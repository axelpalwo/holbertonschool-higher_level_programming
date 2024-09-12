#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
        print("Inside result: {}".format(result))
    except:
        print("Inside result: {}".format(result))
    return result
