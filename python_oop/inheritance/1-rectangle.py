#!/usr.bin/env python3
"""Module Inheritance"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class inheritance"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
