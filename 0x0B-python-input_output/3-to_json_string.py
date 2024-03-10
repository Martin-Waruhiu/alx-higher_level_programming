#!/usr/bin/python3
"""function to serialsize, convert python to
json format"""
import json
"""importing in built json module"""


def to_json_string(my_obj):
    """function definition for seriliazation"""
    return (json.dumps(my_obj))
