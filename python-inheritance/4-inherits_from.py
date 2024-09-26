#!/usr/bin/python3
'''
inherits_from its a function that compares an instance of a class
Returns: True in positive case
'''


def inherits_from(obj, a_class):

    '''
    Returns true or false if an obj is instance of a class
    '''
    if issubclass(obj, a_class) is True:
        return True
    return False
