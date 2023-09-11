#!/usr/bin/python3
"""
same class instance module
"""


def is_same_class(obj, a_class):
    """
    function that checks if object is excactly an instane of
    a specified class

    args:
    obj (obj): object
    a_class (obj): object class
    Return:
    bool: True if instance is same otherwise False
    """
    return type(obj) is a_class
