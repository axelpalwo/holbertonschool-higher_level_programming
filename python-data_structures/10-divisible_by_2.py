#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolean_list = []
    if len(my_list) > 0:
        i = 0
        while i < len(my_list):
            if my_list[i] % 2 == 0:
                boolean_list.append(True)
            else:
                boolean_list.append(False)
            i += 1
    return boolean_list
