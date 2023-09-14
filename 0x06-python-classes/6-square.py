#!/usr/bin/python3
"""
class module
"""


class Square:
    """
    square class module
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        instantation
        """
        self.size = size
        self.position = position

    def area(self):
        """
        returns the area of the square
        """
        return self.size ** 2

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets value to certain position
        """
        if not isinstance(value, tuple) \
        or len(value) != 2 or not all(isinstance(x, int) \
        for x in value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        
        self.__position = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
