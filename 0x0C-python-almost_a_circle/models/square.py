#!/usr/bin/python3
"""
import module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square class, inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor for square class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        return a string representation of the square instance
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width
        )
