#!/usr/bin/python3
"""
write module
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        line = file.write(text)
    return line
