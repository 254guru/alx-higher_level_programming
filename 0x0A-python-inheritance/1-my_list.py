#!/usr/bin/python3
"""
mylist module
"""


class MyList(list):
    """
    class module that inherits from list
    """


    def print_sorted(self):
        """
        instance method that prints list
        """
        if issubclass(MyList, list):
        sorted_list = sorted(self)
        print(sorted_list)
