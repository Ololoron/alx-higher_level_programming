#!/usr/bin/python3
"""Modole contains the function def load_from_json_file"""
import json


def load_from_json_file(filename):
    """ Creates an text Object from a JSON file

    Attr:
        filename (str):name of the file created

    Returns:
        object: object
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
