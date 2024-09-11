#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    coincidence = False
    for okey in a_dictionary:
        if okey is key:
            coincidence = True
    if coincidence is True:
        del a_dictionary[key]
    return a_dictionary
