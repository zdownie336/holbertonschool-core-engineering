#!/usr/bin/env python3
for i in range(100):
    if i < 10:
        num = f"0{i}"
    else:
        num = f"{i}"

    if i < 99:
        print("{number}, ".format(number=num), end='')
    else:
        print("{number}".format(number=num))
