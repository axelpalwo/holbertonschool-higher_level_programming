#!/usr/bin/python3
"""
Este módulo define una clase llamada Square.

La clase Square está diseñada para representar un cuadrado
y tiene un atributo privado
llamado __size que almacenará el tamaño del lado del cuadrado.
"""


class Square:
    """
    Clase Square que representa un cuadrado.

    Esta clase contiene un atributo privado llamado __size,
    que se utiliza para almacenar
    el tamaño de un lado del cuadrado.
    """

    def __init__(self, size=0):
        """
        Inicializa un nuevo objeto de la clase Square.

        Parámetros:
        size (int): El tamaño de un lado del cuadrado (opcional).
        Si no se proporciona, será None.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        # Atributo privado que almacena el tamaño del cuadrado
        def area(self):
            return size