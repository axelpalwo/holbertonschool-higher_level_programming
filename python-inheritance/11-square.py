#!/usr/bin/python3
"""
Clase BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Clase Square que representa un Cuadrado
    """
    def __init__(self, size):
        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
