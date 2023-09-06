#!/usr/bin/python3
"""
Rectangle module
"""
class Rectangle:
    """
    Write an empty class Rectangle that defines a rectangle:

    Args:
        width (int): int
        height (int): int

    Raises:
        TypeError: not an integer
        ValueError: less than 0
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Args:
           value (int): int
        Raises:
            TypeError: not int
            ValueError: less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Args:
           value (int): int
        Raises:
            TypeError: not int
            ValueError: less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ int: area"""
        return self.__width * self.__height

    def perimeter(self):
        """int: perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

