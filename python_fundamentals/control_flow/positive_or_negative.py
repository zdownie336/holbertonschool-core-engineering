#!/usr/bin/env python3

number = __import__("random").randint(-100, 100)

if number < 0:
    print(number, "is negative")
elif number == 0:
    print(number, "is zero")
elif number > 0:
    print(number, "is positive")
