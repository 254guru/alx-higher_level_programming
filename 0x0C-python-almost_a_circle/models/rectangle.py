#!/usr/bin/python3
"""
import module
"""
from models.base import Base


class Rectangle(Base):
    """
    rectangle class, inherits from base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructor for rectangle class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculate and return the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        display the rectangle instance using '#' pound sign
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """
        return a string representation of the rectangle instance
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args):
        """
        updates attributes using arguments in order (id, width, height, x, y)
        """
        args_names = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            if i < len(arg_names):
                setattr(self, arg_names[i], arg)
