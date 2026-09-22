#!/usr/bin/env python3
import calculator_1

if __name__ == "__main__":
    a = 10
    b = 5
    print("{n1} + {n2} = {res}".format(n1=a, n2=b, res=calculator_1.add(a, b)))
    print("{n1} - {n2} = {res}".format(n1=a, n2=b, res=calculator_1.sub(a, b)))
    print("{n1} x {n2} = {res}".format(n1=a, n2=b, res=calculator_1.mul(a, b)))
    print("{n1} / {n2} = {res}".format(n1=a, n2=b, res=calculator_1.div(a, b)))
