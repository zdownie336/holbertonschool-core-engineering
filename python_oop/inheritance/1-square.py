#!/usr/bin/env python3
"""Module for inheritance and polymorphism"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Class for inheritance with square"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
