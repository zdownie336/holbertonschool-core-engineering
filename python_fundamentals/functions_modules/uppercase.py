#!/usr/bin/env python3
def uppercase(str):
    difference = ord("a") - ord("A")
    uppstring = ""
    for char in str:
        code = ord(char)
        if code >= ord("a") and code <= ord("z"):
            letter = chr(code - difference)
            uppstring += letter
        else:
            uppstring += char

    print("{string}".format(string=uppstring))
