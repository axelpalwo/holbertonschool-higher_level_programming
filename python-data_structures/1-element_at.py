#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(my_list) - 1 or idx < 0:
        return None
    elif idx >= 0:
        string = (f"Element at index {idx} is {my_list[idx]}")
        return string

