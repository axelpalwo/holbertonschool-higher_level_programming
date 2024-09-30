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
    """
    open in mode 'a' to append
    write() to write in the file
    json.dumps to convert into string the obj
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
        return
