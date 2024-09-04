#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
    
def uppercase(str):
    i = 0
    char = ''

    if not str:
        return
    
    while i < len(str):
        if islower((str[i])):
            char = chr(ord(str[i]) - 32)
        else:
            char = str[i]
        if i < len(str) - 1:
            print("{}".format(char), end='')
        else:
            print("{}".format(chr(ord(str[i]) - 32)))
        i += 1
