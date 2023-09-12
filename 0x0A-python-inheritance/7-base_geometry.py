#!/usr/bin/python3
"""
class module
"""


class BaseGeometry:
    """
    function that raises exception to a class
    """
    def area(self):
        """
        raise exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        validates value
        args:
        name (str): name of the value
        value (int): value
        Raises:
        TypeError: if value is not an int.
        ValueError: if value is less than or equal to 0
        """

        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
