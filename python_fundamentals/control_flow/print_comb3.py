#!/usr/bin/env python3
for i in range(10):
    for j in range(i + 1, 10):
        if j == 8 and i == 9:
            print("{ten}{one}".format(ten=i, one=j))
        else:
            print("{ten}{one}, ".format(ten=i, one=j), end='')
