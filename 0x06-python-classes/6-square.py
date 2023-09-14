#!/usr/bin/python3
"""
class module
"""


class Square:
    """
    square class module

    Attributes:
        size (int): size
        position (tuple): Tuple
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        instantation

        Args:
            size (int): Description of `param1`.
            position (tuple): Tuple
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (not isinstance(position, tuple) or len(position) != 2
            or not isinstance(position[0], int) or
            not isinstance(position[1], int) or position[0] < 0
                or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        """
        Private instance attribute: size
        """
    def area(self):
        """
        returns area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        returns actual size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        updates size value of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        print function
        """
        if self.__size == 0:
            print("")
        else:
            string_to_print = ""
            for i in range(self.position[1]):
                string_to_print += "\n"
            for x in range(self.size):
                for y in range(self.position[0]):
                    string_to_print += " "
                for z in range(self.size):
                    string_to_print += "#"
                string_to_print += "\n"
            print("{}".format(string_to_print), end='')

    @property
    def position(self):
        """
        positon
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Args:
            value (tuple): value tuple
        Returns:
            Area
        """
        if (not isinstance(value, tuple) or len(value) != 2 or not
            isinstance(value[0], int) or not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
