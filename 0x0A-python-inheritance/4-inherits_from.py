#!/usr/bin/python3
"""
check instance module 3
"""


def inherits_from(obj, a_class):
    """
    function that checks if object is excactly an instane of
    a specified class

    args:
    obj (obj): object
    a_class (obj): object class

    Return:
    bool: True if instance is same otherwise False
    """

    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
