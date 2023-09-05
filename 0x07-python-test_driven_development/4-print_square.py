#!/usr/bin/python3
"""
print square
"""


def print_square(size):
    """
    function that prints a square with the character #.

    Args:
        size (int): size of square

    Raises:
        ValueError: error
        TypeError: error
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

