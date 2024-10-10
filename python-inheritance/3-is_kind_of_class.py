#!/usr/bin/python3
'''
is_kind_of_class its a function that compares classes
Returns: True in positive case
'''


def is_kind_of_class(obj, a_class):

    '''
    Returns true or false if an obj is instance of a class
    '''
    if isinstance(obj, a_class) is True:
        return True
    return False
