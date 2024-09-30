#!/usr/bin/python3
"""
Json library to convert obj into strings and string to objs
"""


import json
"""
Takes a text from a file and converts into an obj
"""


def load_from_json_file(filename):
    """
    open in mode r for reading
    loads to convert
    we return the obj
    """
    with open(filename, 'r', encoding='utf-8') as f:
        obj = json.loads(f.read())
        return obj
