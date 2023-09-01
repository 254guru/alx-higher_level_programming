#!/usr/bin/python3
"""Square Class"""


class Square:
    """
    Attributes:
    size (int): size of square
    """
    def __init__(self, size=0):
        """
        The __init__ method initializes a new square instance with optimal size
        Args:
        size (int): size of square
        Raises:
        TypeError: if size is not int
        ValueError: if size is less than 0
        """
        self.size = size
        """
        Private instance attribute: Size
        """
    def area(self):
        """
        returns current square area
        """
        return self.__size ** 2

    @property
    def size(self):
         """
        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:

        Returns:
            Size
        """
        return self.__size

    @size.setter
    def size(self, value):
          """
        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            value (int): value int
        Returns:
            Area
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
