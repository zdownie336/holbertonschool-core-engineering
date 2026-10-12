#!/usr/bin/env python3
"""This Module is for appending into a file"""


def append_write(filename="", text=""):
    """This Function is for appending into a file"""
    with open(file=filename, mode="a", encoding="UTF-8") as f:
        return f.write(text)
