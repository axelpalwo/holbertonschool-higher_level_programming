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

    def __init__(self, size=None):
        """
        Inicializa un nuevo objeto de la clase Square.

        Parámetros:
        size (int): El tamaño de un lado del cuadrado (opcional).
        Si no se proporciona, será None.
        """
        self.__size = size
        # Atributo privado que almacena el tamaño del cuadrado
