#!/usr/bin/python3
"""
write module
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        line = f.write(text)
    return list
