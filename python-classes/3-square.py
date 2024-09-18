#!/usr/bin/python3
"""
Este módulo define una clase llamada Square.

La clase Square está diseñada para representar un cuadrado y contiene un atributo
privado llamado __size, que almacena el tamaño del lado del cuadrado.
"""

class Square:
    """
    Clase Square que representa un cuadrado.

    Atributos:
        __size (int): El tamaño de un lado del cuadrado, debe ser un entero >= 0.
    """

    def __init__(self, size=0):
        """
        Inicializa un nuevo objeto de la clase Square.

        Parámetros:
        size (int): El tamaño de un lado del cuadrado (por defecto es 0).

        Raises:
        TypeError: Si size no es un entero.
        ValueError: Si size es menor que 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Atributo privado que almacena el tamaño del cuadrado

    def area(self):
        """
        Calcula y devuelve el área del cuadrado.

        Returns:
        int: El área del cuadrado, que es size al cuadrado.
        """
        return self.__size ** 2
