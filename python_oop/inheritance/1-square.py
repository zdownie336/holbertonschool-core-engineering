#!/usr/bin/env python3
"""Module for inheritance and polymorphism"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Square(BaseGeometry):
    """Class for inheritance with square"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
