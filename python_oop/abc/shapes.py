#!/usr/bin/env puthon3

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2

    def perimeter(self):
        return 2 * self.radius * pi


class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (2 * self.width) + (2 * self.height)


def shape_info(Shape):
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")
