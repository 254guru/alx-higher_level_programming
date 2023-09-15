#!/usr/bin/python3
"""
import module
"""
from mpdels.rectangle import Rectangle


class Square(Rectangle):
    """
    square class, inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor for square class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        return a string representation of the square instance
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width
        )
