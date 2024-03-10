#!/usr/bin/python3
"""a function to write to a file"""


def write_file(filename="", text=""):
    """function to write to a file"""

    with open(filename, "w", encoding="UTF-8") as f:
        num_char = f.write(text)
    return (num_char)
