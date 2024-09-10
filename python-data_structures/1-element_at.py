#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(my_list) - 1:
        return None
    elif idx >= 0:
        return (f"Element at index {idx} is {my_list[idx]}")
    else:
        return None
