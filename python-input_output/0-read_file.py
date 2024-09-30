#!/usr/bin/python3
"""
This function opens a file by filename
"""


def read_file(filename=""):
    """
    with statements closes the file after reading
    open(filename) opens the file
    read() reads the contents of the file
    """
    with open(filename) as f:
        print(f.read(), end='')
