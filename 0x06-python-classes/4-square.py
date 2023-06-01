#!/usr/bin/python3

"""
Module Square

Classes:
    Square - A class square
"""


class Square:
    """
    An class square

    Args:
        __size: the size of the square. should be an
        int that's greater than 0
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """get square size"""
        return self.__size

    @size.setter
    def size(self, size):
        """set square size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
