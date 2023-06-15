#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square representation"""
    def __init__(self, size, x=0, y=0, id=None):
        """init the square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, n_size):
        self.width = n_size
        self.height = n_size

    def update(self, *args, **kwargs):
        """updates the rectangle instance arguments"""
        if args and len(args) != 0:
            for i in range(0, len(args)):
                if i + 1 == 1:
                    self.id = args[i]
                elif i + 1 == 2:
                    self.size = args[i]
                elif i + 1 == 3:
                    self.x = args[i]
                elif i + 1 == 4:
                    self.y = args[i]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        """return the string representation of the square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """return the dictionary representation of the instance"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
