#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    while i < list_length:
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except (TypeError, ZeroDivisionError, ValueError):
            result = 0
            if i >= len(my_list_2) or i >= len(my_list_1):
                print('out of range')
            elif my_list_2[i] == 0:
                print('division by 0')
            else:
                print('wrong type')
        finally:
            new_list.append(result)
        i += 1

    return new_list
