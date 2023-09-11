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
        sorted_list = super().copy()
        sorted_list.sort()
        print(sorted_list)
