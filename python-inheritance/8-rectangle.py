#!/usr/bin/python3
'''
Base Geometry Class
'''


class BaseGeometry:
    '''
    Base Geometry object
    '''
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')

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
