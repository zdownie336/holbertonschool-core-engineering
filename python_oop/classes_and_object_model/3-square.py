#!/usr/bin/env python3
"""This module defines a square class"""


class Square:
    """This class represents a square"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        return self.__size**2
