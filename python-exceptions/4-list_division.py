#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            print('out of range')
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            print('wrong type')
        finally:
            new_list.append(result)
    return new_list
