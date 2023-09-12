#!/usr/bin/python3
"""
read file module
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

    except FileNotFoundError:
        print(f"file '{filename}' not found.")
    except Exception as e:
        print(f"An error occured: {str(e)}")
