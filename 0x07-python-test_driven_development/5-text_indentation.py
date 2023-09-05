#!/usr/bin/python3
"""
module print two new lines
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after 
    each of these characters: ., ? and :
    Args:
        text (str): a line of text(string)
    Raises:
        TypeError: error
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    
    leading_whitespace = False

    for char in text:
        if char in ['.', '?', ':']:
            result += char + '\n\n'
            leading_whitespace = True
        elif char == '\n':
            leading_whitespace = False
        elif char != ' ':
            result += char
            leading_whitespace = False
        elif char == ' ' and not leading_whitespace:
            result += char

    print(result)
