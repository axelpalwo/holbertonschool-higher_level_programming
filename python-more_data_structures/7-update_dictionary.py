#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    repeat = False
    for okey in a_dictionary:
        if okey == key:
            repeat = True
            a_dictionary[okey] = value
        else:
            a_dictionary[okey] = a_dictionary[okey]
    if repeat == False:
        a_dictionary[key] = value
    return a_dictionary
