#!/usr/bin/env python3
"""This Module is for reading a file"""


def read_file(filename=""):
    """This Function is for reading a file's content"""
    with open(filename) as f:
        print(f.read(), end="")
