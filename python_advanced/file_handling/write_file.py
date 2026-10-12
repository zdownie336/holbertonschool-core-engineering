#!/usr/bin/env python3
"""This Module is for writing into a file"""


def write_file(filename="", text=""):
    """This Function is for writing into a file"""
    with open(file=filename, mode="w", encoding="UTF-8") as f:
        return f.write(text)
