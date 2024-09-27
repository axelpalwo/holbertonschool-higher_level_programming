#!/usr/bin/python3
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
