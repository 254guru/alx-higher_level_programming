#!/usr/bin/python3
"""
classs module
"""


class MyInt(int):
    """
    myint module
    """

    def __eq__(self, other):
        """
        invert behavior of the == operator
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        invert the behavior of the != operator
        """
        return not super().__ne__(other)
