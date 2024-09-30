#!/usr/bin/python3
"""
Json library to convert obj into strings and string to objs
"""


import json
"""
Converts a string into an object
"""


def from_json_string(my_str):
    """
    We use Json library and Load method to obtain an obj from a string
    """
    return json.loads(my_str)
