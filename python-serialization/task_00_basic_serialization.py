#!/usr/bin/python3
"""
Json library to convert obj into strings and string to objs
"""


import json
"""
serialize_and_save_to_fil takes an obj and saves it in a file
"""


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data))
        return
"""
load_and_deserialize takes a file and converts its contents
in a python object
"""


def load_and_deserialize(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        obj = json.loads(f.read())
        return obj
