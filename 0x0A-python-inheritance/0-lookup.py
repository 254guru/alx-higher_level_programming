#!/usr/bin/python3
"""
function that returns list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    lookup: uses python's builtin dir() function to
    retrieve the list of available attributes and methods of an object

    obj: object to print contents of dir

    return list
    """
    attributes_and_methods = dir(obj)
    filtered_attributes_and_methods = [item for item in attributes_and_methods \
            if not item.startswith('--')]
    return filtered_attributes_and_methods
