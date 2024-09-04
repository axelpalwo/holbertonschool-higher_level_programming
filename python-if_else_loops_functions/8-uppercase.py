#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        if i < len(str) - 1:
            print("{}".format(chr(ord(str[i]) - 32)), end='')
        else:
            print("{}".format(chr(ord(str[i]) - 32)))
        i += 1
