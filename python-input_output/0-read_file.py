#!/usr/bin/python3
"""
This function opens a file by filename
"""


def read_file(filename=""):
    with open(filename) as f:
        print(f.read())
