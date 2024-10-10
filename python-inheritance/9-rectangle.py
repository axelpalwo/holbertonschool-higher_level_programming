#!/usr/bin/python3
"""
Clase BaseGeometry
"""


BaseGeometry = Rectangle = __import__('7-base_geometry').BaseGeometry
"""
Este módulo define una clase llamada Rectangle.
"""


class Rectangle(BaseGeometry):
    """
    Clase Rectangle que representa un Rectangulo
    """
    def __init__(self, width, height):
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
