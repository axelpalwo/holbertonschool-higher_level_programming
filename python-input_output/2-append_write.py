#!/usr/bin/python3
"""
This function appends on the end of a file
"""


def append_write(filename="", text=""):
    """
    mode 'a' appends at the end of a file
    write(text) writes on the file and returns the number of chars written
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
