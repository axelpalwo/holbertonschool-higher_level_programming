#!/usr/bin/python3
"""
Json library to convert obj into strings and string to objs
"""


import json
"""
save to json file takes an obj converts it into a string
and then saves it in a file
"""


def save_to_json_file(my_obj, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
        return
