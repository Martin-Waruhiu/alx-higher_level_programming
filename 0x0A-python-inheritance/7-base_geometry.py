#!/usr/bin/python3
"""defining the geometry class with a area method"""


class BaseGeometry:
    """class definition"""

    def area(self):
        """area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """intger validating method"""

        self.name = name
        self.value = value
        if not isinstance(self.value, int):
            raise TypeError("<name> must be an integer")
        if (self.value <= 0):
            raise ValueError("<name> must be greater than 0")
