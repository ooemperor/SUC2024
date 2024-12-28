"""
Immoscout Parse
This script is responsible for parsing the immoscout listings and saving the results in the database
"""
import bs4 as bs
from tqdm import tqdm
import os
import re
import yake
from generics import merge_dicts
from immoscout_db import write_immoscout_kaufen_to_DB, write_immoscout_mieten_to_DB, execute_sql_immo_DB
from config import config
from multiprocessing import Process, Queue, Semaphore


def parse_dl(dl_listing) -> dict:
    """
    parse a given thml site form immoscout into usable dict data
    :param dl_listing: The data list of the listing
    :return:
    """
    keys = []
    values = []
    result_dict = {}

    for dlitem in dl_listing.find_all("dt"):
        keys.append(dlitem.text)

    for ddItem in dl_listing.find_all("dd"):
        values.append(ddItem.text.replace("'", "''"))

    for i in range(len(keys)):
        key = keys[i].replace(":", "")
        result_dict[key] = values[i]

    return result_dict


def get_dict_value_for_DB(data, keyword) -> str:
    """
    Prepares a dictionary value for insertion in the database or and empty value
    and escapes the single quote
    :param data: The data dictionary
    :type data: dict
    :param keyword: The keywords to fetch teh value for
    :type keyword: str
    :return: The prepared dictionary value
    :rtype: str
    """
    return data.get(keyword, '''''').replace("'", "\'")


def get_keywords(description: str) -> list:
    """
    Extracts the most important keywords out of the description.
    :param description: The description of the immoscout listing
    :type description: str
    :return: The list of keywords
    :rtype: list
    """
    language = "de"
    max_ngram_size = 3
    deduplication_threshold = 0.9
    numOfKeywords = 20
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(description)
    return keywords


def parse_property_page(site_data, listing, debug=False) -> dict:
    """
    Function to parse the property page and return the properties  as a dicitionary
    :param site_data: The site data as html
    :param listing: The listing name for use in fullId
    :param debug: bool param to indicate if we want to print or not
    :return: The properties dict
    """
    soup = bs.BeautifulSoup(site_data, "html.parser")
    listing = listing.replace(".html", "")
    name_arr = listing.split("_")
    identifiers = {"type": name_arr[1], "id": name_arr[2], "fullId": f"/{name_arr[1]}/{name_arr[2]}"}

    # search for the listing tables
    listings = soup.find_all("dl")

    description = {}
    descriptions = soup.find_all("h2")
    for desc in descriptions:
        if desc.text == "Beschreibung":
            description["description"] = desc.find_next().text.replace("'", "''")

    address_data = []
    for tag in soup.find_all("address")[0]:
        address_data.append(tag.string.strip().replace(",", ""))

    address = {"street": address_data[0].replace("'", "''"), "city": address_data[1].replace("'", "''")}

    # grab title
    title = soup.title.text
    title = {"title": title.replace(" | ImmoScout24", "").replace("'", "''")}

    miete = parse_dl(listings[0])
    for val in miete.keys():
        miete[val] = re.sub("[^0-9]", "", miete[val])
        # miete[val] = miete[val].replace("CHF ", "")
        # miete[val] = miete[val].replace("EUR ", "")
        # miete[val] = miete[val].replace(".– ", "")
        # miete[val] = miete[val].replace("/Woche", "")
    main_data = parse_dl(listings[1])
    listing_details = parse_dl(listings[2])
    output = merge_dicts(miete, main_data, title, listing_details, address, description, identifiers)
    if debug:
        print(output)

    return output


def parser_worker(queue: Queue, semaphore: Semaphore):
    """
    Implementation of a worker who will parse a single immoscout listing
    :param queue: The queue to retreive listings from
    :type queue: Queue
    :param semaphore: The semaphore used for sync between master and workers
    :type semaphore: Semaphore
    :return: None
    """
    try:
        while True:
            listing = queue.get()
            if listing is None:
                break
            parse_and_insert_listing_in_db(listing)
            semaphore.release()

    except Exception as e:
        semaphore.release()
        raise e


def parse_immoscout_listings(search_word: str) -> None:
    """
    Parses all the immoscout listing present in the filesystem and pushes them into the database
    :param search_word: String to filter in the listing name (e.g. kaufen or mieten)
    :type search_word: str
    :return: None
    """
    listings = os.listdir("../data/immoscout/listings")

    queue = Queue()
    semaphore = Semaphore(config.max_concurrent_parsers)

    # Start worker processes
    workers = []
    for _ in range(config.max_concurrent_parsers):
        p = Process(target=parser_worker, args=(queue, semaphore))
        p.start()
        workers.append(p)

    # Add tasks to the queue
    for listing in tqdm(listings):
        if search_word in listing:
            semaphore.acquire()
            queue.put(listing)
        else:
            continue

    for _ in range(config.max_concurrent_parsers):
        queue.put(None)

    # Wait for everyone to finish
    for p in workers:
        p.join()


def parse_and_insert_listing_in_db(listing: str) -> None:
    """
    Parses and inserts the immoscout listing into the database
    :param listing: The listing to parse and insert into the databse
    :type listing: str
    :return: None
    """
    f = open(f"../data/immoscout/listings/{listing}", "rb")
    data = f.read()
    f.close()
    listing_data = parse_property_page(data, listing)
    keywords = get_keywords(listing_data["description"])

    if listing_data["type"] == "kaufen":
        write_immoscout_kaufen_to_DB(listing_data)
        write_immoscout_keyword(keywords, listing_data["fullId"])

    elif listing_data["type"] == "mieten":
        write_immoscout_mieten_to_DB(listing_data)
        write_immoscout_keyword(keywords, listing_data["fullId"])

    else:
        raise Exception(f"Unexpected type {listing_data['type']}")


def write_immoscout_keyword(keywords: list, listing: str) -> None:
    """
    Calls the insert function into the database
    :param keywords: The keywords to insert into the database
    :type keywords: list
    :param listing: the listing id
    :type listing: str
    :return: None
    """

    if len(keywords) > 0:
        insert_sql = f"INSERT INTO stage.immoscout_keywords (fullId, keyword) VALUES ('{listing}', '{keywords[0][0]}')"
        for i in range(1, len(keywords)):
            insert_sql += f",('{listing}', '{keywords[i][0]}')"

        execute_sql_immo_DB(insert_sql)


if __name__ == "__main__":
    execute_sql_immo_DB("TRUNCATE TABLE stage.immoscout_kaufen;")
    execute_sql_immo_DB("TRUNCATE TABLE stage.immoscout_keywords")
    execute_sql_immo_DB("TRUNCATE TABLE stage.immoscout_mieten;")
    parse_immoscout_listings("")
