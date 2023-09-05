#!/usr/bin/python3
"""
add_integer
add two integers a and b
"""


def add_integer(a, b=98):
    """
    function that adds two integers or floats
    Args:
        a (number): Float or Number
        b (:obj:number:optional): Optional Float or Integer

    Raises: TypeError: If not float or integer

    Returns Integer or float
    """
    if not(isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a + b)
