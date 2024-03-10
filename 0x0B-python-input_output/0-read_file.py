#!/usr/bin/python3
"""function to read from a file"""


def read_file(filename=""):
    """function definition to read from the file"""
    with open(filename, "r", encoding="UTF-8") as file:
        data = file.read()
        print(data)
