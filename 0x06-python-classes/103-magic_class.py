#!/usr/bin/python3
"""defines MagicClass implementation"""
import dis
import math


class MagicClass:
    """After reverse engineering the bytecode. the magic class turns out to be a class for a circle"""
    def __init__(self, radius = 0):
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """returns the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """returns the circumference of the circle"""
        return 2 * math.pi * self.__radius

if __name__ == "__main__":
    dis.dis(MagicClass)
