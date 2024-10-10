#!/usr/bin/python3
"""
Converts a class into a json obj
"""


def class_to_json(obj):
    """
    We access the dir method of a Class
    """
    return vars(obj)
