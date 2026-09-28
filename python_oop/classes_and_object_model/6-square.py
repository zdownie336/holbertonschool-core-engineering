#!/usr/bin/env python3
"""This module defines a square class"""


class Square:
    """This class represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        if type(position) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        voffset = "\n" * self.__position[0]
        hoffset = " " * self.__position[1]

        print(voffset, end='')
        for i in range(self.__size):
            print(hoffset, end="")
            for j in range(self.__size):
                print("#", end="")
            print("")

    def __str__(self):
        square = ""
        if self.__size == 0:
            return square

        voffset = "\n" * self.__position[1]
        hoffset = " " * self.__position[0]

        square += voffset
        for i in range(self.__size):
            square += hoffset
            for j in range(self.__size):
                square += "#"
            if i < self.__size - 1:
                square += "\n"

        return square
