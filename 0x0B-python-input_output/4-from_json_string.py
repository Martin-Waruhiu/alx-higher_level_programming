#!/usr/bin/python3
"""a function to convert json to python format"""

import json
"""import json module"""


def from_json_string(my_str):
    """function definition for desreriazailation"""
    return (json.loads(my_str))
