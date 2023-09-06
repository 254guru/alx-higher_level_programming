#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """
    an empty class Rectangle that defines a rectangle:

    Args:
        width (int): int
        height (int): int

    Raises:
        TypeError: not an integer
        ValueError: less than 0
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """int: area"""
        return self.__width * self.__height

    def perimeter(self):
        """int: perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """str: rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """str: function call"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """print"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area
        Args:
            rect_1 (Rectangle): one
            rect_1 (Rectangle): one

        Raises:
            TypeError: not Rectangle

        Returns:
            Rectangle: biggest or rect_1 if equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        returns a new Rectangle isinstance

        Args:
            size (int): int size
        """
        return cls(size, size)
