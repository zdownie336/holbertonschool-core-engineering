#!/usr/bin/env python3


def element_at(my_list, idx):
    for char in my_list:
        if idx < 0 or idx > len(my_list):
            return None
        else:
            char = my_list[idx]
            return char
