#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    counter = 0
    if x > len(my_list):
        x = len(my_list)
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            i += 1
        except:
            i += 1
            counter += 1
    print()
    return i - counter
