#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class representation.
    Represents a rectangle and inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """init base class and set properties
        Attributes:
            width: rectangle width
            height: rectangle height
            x: x position
            y: y position
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, n_x):
        """setter for x"""
        if type(n_x) is not int:
            raise TypeError("x must be an integer")
        elif n_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = n_x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, n_y):
        """setter for y"""
        if type(n_y) is not int:
            raise TypeError("y must be an integer")
        elif n_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = n_y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, n_width):
        """setter for width"""
        if type(n_width) is not int:
            raise TypeError("width must be an integer")
        elif n_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = n_width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, n_height):
        """setter for height"""
        if type(n_height) is not int:
            raise TypeError("height must be an integer")
        elif n_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = n_height

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """return the string representation of the rectangle instance"""
        id = self.id
        width = self.width
        height = self.height
        x = self.x
        y = self.y

        return f"[Rectangle] ({id}) {x}/{y} - {width}/{height}"

    def update(self, *args, **kwargs):
        """updates the rectangle instance arguments"""
        if args and len(args) != 0:
            for i in range(0, len(args)):
                if i + 1 == 1:
                    self.id = args[i]
                elif i + 1 == 2:
                    self.width = args[i]
                elif i + 1 == 3:
                    self.height = args[i]
                elif i + 1 == 4:
                    self.x = args[i]
                elif i + 1 == 5:
                    self.y = args[i]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """return the dictionary representation of the instance"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
