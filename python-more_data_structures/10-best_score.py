#!/usr/bin/python3
def best_score(a_dictionary):
    bigkey = None
    bigval = 0
    if a_dictionary is not None:
        for key in a_dictionary:
            if bigval < a_dictionary[key]:
                bigval = a_dictionary[key]
                bigkey = key
    return bigkey
