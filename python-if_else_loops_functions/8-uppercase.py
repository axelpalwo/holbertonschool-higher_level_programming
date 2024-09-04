#!/usr/bin/python3
def uppercase(str):
    for i in len(str):
        if i != len(str):
            print("{}".format(ord(i) - 32), end='')
        else:
            print("{}".format(ord(i) - 32))
