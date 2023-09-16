#!/usr/bin/python3
"""
import modules
"""
import json
from os import path


class Base:
    """
    base class for managing id attributes in derived classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor for base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert a list of dictionaries to a json string
        """
        if list_dictionaries is Nne or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
