#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_value = 0
    b_value = 0

    if len(tuple_a) > 0:
        a_value += tuple_a[0]
    if len(tuple_b) > 0:
        a_value += tuple_b[0]

    if len(tuple_a) >= 2:
        b_value += tuple_a[1]
    if len(tuple_b) >= 2:
        b_value += tuple_b[1]

    return (a_value, b_value)
