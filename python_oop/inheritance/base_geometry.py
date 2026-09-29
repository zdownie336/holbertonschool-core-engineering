#!/usr/bin/env python3


class Errors(Exception):
    pass


class BaseGeometry:

    def area(self):
        raise Errors('area() not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            self.value = value
