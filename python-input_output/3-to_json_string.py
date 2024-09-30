#!/usr/bin/python3
"""
Json library to convert obj into strings and string to objs
"""


import json
"""
Converts an object into a string
"""


def to_json_string(my_obj):
    """
    We use Json library and Dump method to stringify the obj
    """
    return json.dumps(my_obj)
