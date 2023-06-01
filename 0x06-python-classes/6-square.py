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
    def __init__(self, size=0, position=(0, 0)):
        self.position = position
        self.size = size

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

    @property
    def position(self):
        """get square position"""
        return self.__position

    @position.setter
    def position(self, position):
        if (not isinstance(position, tuple)
                or len(position) != 2
                or not all(isinstance(num, int) for num in position)
                or not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """ prints a square of side length `size`"""
        if self.size == 0:
            print()
        else:
            for i in range(0, self.position[1]):
                print()

            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")

                for j in range(self.size):
                    print("#", end="")
                print()
