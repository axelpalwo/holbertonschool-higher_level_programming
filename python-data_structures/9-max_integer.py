#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = 0
    i = 0
    while i < len(my_list):
        if max_num < my_list[i]:
            max_num = my_list[i]
        i += 1

