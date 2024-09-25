#!/usr/bin/python3
'''
MyList class, its a list
'''


class MyList(list):

    '''
    This method prints the list sorted
    '''
    def print_sorted(self):
        print(sorted(self))
