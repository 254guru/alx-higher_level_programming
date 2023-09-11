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
        sorted_list = sorted(self)
        for item in sorted_list:
            print(item, end=' ')
        print()
