#!/usr/bin/python3
"""
sam class instance 2
"""


def is_kind_of_class(obj, a_class):
    """
    function that checks if object is an instane of class
    inherited from a specified class

    args:
    obj (obj): object
    a_class (obj): object class

    Return:
    bool: True if instance is same otherwise False
    """

    return isinstance(obj, a_class)
