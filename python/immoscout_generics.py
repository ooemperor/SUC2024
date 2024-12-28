"""
Immoscout Generics
Script that contains generic functions for use in immoscout scripts
"""
import os
import requests


def read_from_website(url: str) -> str:
    """
    read plain result from url
    :param url: the url to visit
    :type url: str
    :return: the html of the site
    :rtype: str
    """
    headers = {
        'User-Agent': 'PostmanRuntime/7.42.0'  # This is another valid field
    }
    result = requests.get(url, headers=headers)
    try:
        assert result.status_code == 200
        return result.text
    except AssertionError as e:

        if result.status_code == 404:
            return ""
        else:
            print(result.text)
            print(result.status_code)
            print(url)
            raise e


def write_object_id(id_: str) -> None:
    """
    write the object_id in the file
    :param id_: the id of the object
    :type id_: str
    :return: None
    """
    fa = open("../data/immoscout/object_ids.txt", "a")

    with open("../data/immoscout/object_ids.txt", "r") as f:
        skipping = False
        for line in f.readlines():

            if id_ in line:
                skipping = True

        if not skipping:
            fa.write(id_ + "\n")
        f.close()
        fa.close()


def write_listing_tofile(listing_id: str, listing: str) -> None:
    """
    write the listing in file
    :param listing_id: the id of the listing
    :type listing_id: str
    :param listing: the html of the listing
    :type listing: str
    :return: None
    """
    try:
        f = open(f"../data/immoscout/listings/{listing_id}.html", "w+")
        f.write(listing)
        f.close()

    except UnicodeEncodeError as e:
        f.close()
        if os.path.exists(f"../data/immoscout/listings/{listing_id}.html"):
            os.remove(f"../data/immoscout/listings/{listing_id}.html")