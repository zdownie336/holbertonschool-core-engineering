#!/usr/bin/env python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    print("{n1} + {n2} = {res}".format(n1=a, n2=b, res=add(a, b)))
    print("{n1} - {n2} = {res}".format(n1=a, n2=b, res=sub(a, b)))
    print("{n1} x {n2} = {res}".format(n1=a, n2=b, res=mul(a, b)))
    print("{n1} / {n2} = {res}".format(n1=a, n2=b, res=div(a, b)))
