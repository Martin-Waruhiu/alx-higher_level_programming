#!/usr/bin/python3
"""function that creates and object from a json file"""

import json
"""import built in json module"""


def load_from_json_file(filename):
    """function that creates and object fro a json file"""
    with open(filename) as f:
        return (json.load(f))
