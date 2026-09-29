#!/usr/bin/env python3
"""Module: Square."""


class Square:
    """Initiate square class with size and position attribute"""

    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if len(position) != 2 and len(position):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (
            isinstance(position[0], int) is False
            or isinstance(position[1], int) is False
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def __str__(self):
        square = ""
        if self.__size == 0:
            return square
        else:
            i = 0
            for line in range(self.position[1]):
                square = square + "\n"
            for index in range(self.__size):
                for row in range(self.position[0]):
                    square = square + " "
                for index in range(self.__size):
                    square = square + "#"
                if i < self.__size - 1:
                    square = square + "\n"
                i = i + 1
            return square

    def my_print(self):
        print(self)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def size(self):
        return self.__size

    @position.setter
    def position(self, size):
        self.__size = size

    def area(self):
        return self.__size * self.__size
