#!/usr/bin/python3
"""
append after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file
    """
    modified_lines = []

    with open(filename, 'r') as file:
        for line in file:
            modified_lines.append(line)
            
            if search_string in line:
                modified_lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(modified_lines)
