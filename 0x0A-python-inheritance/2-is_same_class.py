#!/usr/bin/python3
"""function to check if an object belongs to
a certain class"""


def is_same_class(obj, a_class):
    """method to check type of object"""

    if type(obj) == a_class:
        return True
    return False
