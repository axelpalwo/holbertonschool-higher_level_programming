#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    if len(my_list) > 0:
        new_list = set(my_list)
        for num in new_list:
            total += num
    return total
