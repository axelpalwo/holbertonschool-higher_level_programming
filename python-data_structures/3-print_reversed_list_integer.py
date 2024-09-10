#!/usr/bin/python3
def print_reversed_list_integers(my_list=[]):
    my_list.reverse()
    i = 0
    while i < len(my_list):
        print("{}".format(my_list[i]))
