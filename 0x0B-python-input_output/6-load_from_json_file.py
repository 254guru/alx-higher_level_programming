#!/usr/bin/python3
"""
import module
"""


import json
"""
json module
"""


def load_from_json_file(filename):
    """
    function that creates an object from a json file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        my_obj = json.load(file)
    return my_obj
