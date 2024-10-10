#!/usr/bin/python3
'''
MyList class, its a list
'''


class MyList(list):

    '''
    This method prints the list sorted
    '''

    def print_sorted(self):
        """Imprime una lista ordenada."""
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list
