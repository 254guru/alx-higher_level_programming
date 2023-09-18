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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save a list of objects to ba json file
        """
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attrs = []

            for elem in list_objs:
                json_attrs.append(elem.to_dictionary())

            return f.write(cls.to_json_string(json_attrs))
