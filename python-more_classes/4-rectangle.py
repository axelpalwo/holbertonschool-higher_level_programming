#!/usr/bin/python3
"""
Este módulo define una clase llamada Square.
"""

# 0-Rectangle: Clase vacia
class Rectangle:
    """
    Clase Square que representa un Rectangulo
    """
    # 1-Rectangle: __init__, setters & getters de width y height
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    # 2-Rectangle: Area y Perimetro
    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)
    # 3-Rectangle: __str__ y __repr__
    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = []
        for _ in range(self.__height):
            rectangle.append("#" * self.__width)
        return "\n".join(rectangle)
    # 4-Rectangle: Debe devolver un string con lo necesario
    # para formar un nuevo objeto rectangulo
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
