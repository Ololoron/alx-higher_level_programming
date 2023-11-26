#!/usr/bin/python3
"""Module has a function from_json_string that returns an object. """
import json


def from_json_string(my_str):
    """Function returns an object represented by a JSON string.

    Attr:
        my_str (str): json obj to convert to python object.

    Return:
        type: Python objects.

    """
    # print("type json.loads(my_str)--> {}".format(type)json.loads(my_str)))
    # print("type my_str--> {}".format(type(my_str)))

    return json.loads(my_str)
