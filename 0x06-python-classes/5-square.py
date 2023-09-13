#!/usr/bin/python3
"""
class module
"""


class Square:
    """
    square class module
    """

    def __init__(self, size=0):
        """
        initialize size value of the square
        """
        self.__size = size

    def area(self):
        """
        return current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        return actual size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter method: updates the size value of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
