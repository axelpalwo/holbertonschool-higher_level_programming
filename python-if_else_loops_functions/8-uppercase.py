#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
    
def uppercase(str):
    i = 0
    while i < len(str):
        if islower((str[i])):
            if i < len(str) - 1:
                print("{}".format(chr(ord(str[i]) - 32)), end='')
            else:
                print("{}".format(chr(ord(str[i]) - 32)))
        else:
            print(f"{str[i]}", end='')
        i += 1
