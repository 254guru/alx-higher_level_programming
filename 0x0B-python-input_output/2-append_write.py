#!/usr/bin/python3
"""
append file
"""


def append_write(filename="", text=""):
    """
    function that appends a string at end of text file
    """
    with open(filename, 'a', encoding="utf-8") as file:
        line = file.write(text)
    return line
