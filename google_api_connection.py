""" A list of methods which integrate with Google APIs"""

import json
import requests

BASE_URI = "https://www.googleapis.com/books/v1/volumes"


def get_volumes(query: str):
    """ Get list of items that match the requested query"""
    response = requests.get(f"{BASE_URI}?q={query}", timeout=1000)
    return json.loads(response.text)


def get_volume_info(volume_id: str):
    """ Get specific information about the provided volume_id"""
    response = requests.get(f"{BASE_URI}/{volume_id}", timeout=1000)
    return json.loads(response.text)
