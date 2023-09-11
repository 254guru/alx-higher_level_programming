#!/usr/bin/python3
"""
mylist module
"""


class MyList(list):
    """
    class module that inherits list
    """

    def print_sorted(self):
        """
        instance method that prints list
        """
        if issubclass(MyList, list):
            print(sorted(self))
