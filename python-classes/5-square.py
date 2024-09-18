#!/usr/bin/python3
"""
Este módulo define una clase llamada Square.

La clase Square está diseñada para representar un cuadrado
y contiene un atributo
privado llamado __size, que almacena el tamaño del lado del cuadrado.
Proporciona métodos para obtener y modificar el tamaño del cuadrado y para
calcular su área.
"""


class Square:
    """
    Clase Square que representa un cuadrado.

    Atributos:
        __size (int): El tamaño de un lado del cuadrado,
        debe ser un entero >= 0.
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
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """
        Getter del atributo size.

        Returns:
        int: El tamaño del lado del cuadrado.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter del atributo size.

        Parámetros:
        value (int): El nuevo valor para el tamaño del cuadrado.

        Raises:
        TypeError: Si value no es un entero.
        ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calcula y devuelve el área del cuadrado.

        Returns:
        int: El área del cuadrado, que es size al cuadrado.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Imprime un cuadrado en la consola utilizando el carácter '#',
        de acuerdo con el tamaño actual.

        Si el valor de __size es 0, no se imprime nada. De lo contrario,
        imprime un cuadrado formado
        por filas y columnas del carácter '#', donde el número de filas y
        columnas es igual al valor 
        de __size.

        Ejemplo:
        Si __size es 3, el resultado será:
        ###
        ###
        ###

        Si __size es 0, no se imprime nada.
        """
        if self.__size != 0:
            for i in range(self.__size):
                for v in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
