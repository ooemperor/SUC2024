"""
Immoscout Load
This script is responsible for loading the immoscout listings and saving them for later processing
"""
import os
import bs4 as bs
from tqdm import tqdm
from immoscout_generics import read_from_website, write_object_id, write_listing_tofile


def find_immoscout_links(site_data: str):
    """
    Parse the important data out of the immoscout listing
    :param site_data: The raw html out of the file
    :type site_data: str
    :return:
    """
    object_ids = []
    soup = bs.BeautifulSoup(site_data, "html.parser")
    links = soup.find_all("a")
    for link in links:
        value = link.get("href")
        if value.startswith("/mieten/") or value.startswith("/kaufen/"):
            object_ids.append(value)

    return object_ids


def search_immoscout_listings(location: str) -> None:
    """
    Search for the object ids in immoscout given by location
    :param location: The location to go search for
    :type location: str
    :return: None
    """
    for i in tqdm(range(1, 51)):
        data = read_from_website(f"https://rest-api.immoscout24.ch/de/immobilien/mieten/ort-{location}?pn={i}")
        object_ids = find_immoscout_links(data)
        for object_id in object_ids:
            write_object_id(object_id)
        # time.sleep(5)

        data = read_from_website(f"https://rest-api.immoscout24.ch/de/immobilien/kaufen/ort-{location}?r=50000&pn={i}")
        object_ids = find_immoscout_links(data)
        for object_id in object_ids:
            write_object_id(object_id)


def search_location_listings():
    """
    Fetches all the listings for the given regions.
    :return: None
    """
    locations = ["biel-bienne", "bern", "fribourg", "neuchatel", "solothurn", "olten", "luzern", "thun", "zuerich",
                 "lyss", "zollikofen"]

    for location in locations:
        print(f"### {location} ###")
        search_immoscout_listings(location)


def fetch_immoscout_listing() -> None:
    """
    Fetch the listings for immoscout
    Which listings to fetch is defined in a file in the filesystem
    Writes down the raw listing to the filesystem
    :return: None
    """
    already_fetched = []
    already_fetched_raw = os.listdir("../data/immoscout/listings")

    for listing in already_fetched_raw:
        already_fetched.append(listing.replace(".html", "").replace("_", "/"))

    f = open("../data/immoscout/object_ids.txt", "r")
    for line in tqdm(f.readlines()):
        if line.strip() in already_fetched:
            continue
        else:
            # needs to be fetched
            result = read_from_website(f"https://rest-api.immoscout24.ch/{line.strip()}")
            try:
                write_listing_tofile(line.strip().replace("/", "_"), result)
            except Exception as e:
                print(e)

            # time.sleep(1)
            pass


if __name__ == "__main__":
    search_location_listings()
    fetch_immoscout_listing()
