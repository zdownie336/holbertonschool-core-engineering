#!/usr/bin/env python3

from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    result = add(a, b)
    print("{num1} + {num2} = {result}".format(num1=a, num2=b, result=result))
