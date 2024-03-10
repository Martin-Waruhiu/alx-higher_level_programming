#!/usr/bin/python3
"""function to read from a file"""


def read_file(filename=""):
    """function definition to read from the file"""

    with open(filename, "r", encoding="UTF-8") as file:
        """function to open the file before reading it"""
        print(file.read(), end="")
