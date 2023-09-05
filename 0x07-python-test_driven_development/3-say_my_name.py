#!/usr/bin/python3
"""
print names module
"""


def say_my_name(first_name, last_name=""):
    """
    function prints name according to first and last basis
    Args:
    first_name (str): first name
    last_name (str): last name

    Raises:
    TypeError: if first and last names aren't strings
    """
    # Check if first_name and last_name are strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the message
    print("My name is {} {}".format(first_name, last_name))

