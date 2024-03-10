#!/usr/bin/python3
""" function that writes an Object to a text file
using a JSON representation"""

import json
"""import module json for seriliazation"""


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file
, using a JSON representation"""
    with open(filename, "w") as f:
        return (f.write(json.dumps(my_obj)))
