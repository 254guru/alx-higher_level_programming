#!/usr/bin/python3
"""
module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square module
    """
    def __init__(self, size):
        """inherit function"""
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        square description return function
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
