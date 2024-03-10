#!/usr/bin/python3
"""Function to append to a file"""


def append_write(filename="", text=""):
    """apeend to  a file defintion"""
    with open(filename, "a", encoding="UTF-8") as f:
        num_char = f.write(text)
        return(num_char)
