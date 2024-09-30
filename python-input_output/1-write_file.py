#!/usr/bin/python3
"""
This function writes on a file
"""


def write_file(filename="", text=""):
    """
    write(text) writes on the file and returns the number of chars written
    """
    with open(filename,'w', encoding='utf-8') as f:
        return f.write(text)
