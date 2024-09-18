#!/usr/bin/python3
"""
Este módulo define una clase llamada Square.

La clase Square está diseñada para representar un cuadrado
y contiene un atributo privado llamado __size, que almacena
el tamaño del lado del cuadrado. Proporciona métodos para obtener
y modificar el tamaño del cuadrado y para calcular su área.
"""


class Square:
    """
    Clase Square que representa un cuadrado.

    Atributos:
        __size (int): El tamaño de un lado del cuadrado, debe ser
                      un entero >= 0.
        __position (tuple): La posición del cuadrado en una cuadrícula,
                            debe ser una tupla de dos enteros positivos.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Inicializa un nuevo objeto de la clase Square.

        Parámetros:
        size (int): El tamaño de un lado del cuadrado (por defecto es 0).
        position (tuple): La posición del cuadrado en una cuadrícula
                          (por defecto es (0, 0)).

        Raises:
        TypeError: Si size no es un entero o si position no es una
                   tupla de dos enteros positivos.
        ValueError: Si size es menor que 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if not (isinstance(position, tuple) and
                len(position) == 2 and
                all(isinstance(x, int) for x in position) and
                all(x >= 0 for x in position)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """
        Getter del atributo position.

        Returns:
        tuple: La posición del cuadrado en la cuadrícula.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter del atributo position.

        Parámetros:
        value (tuple): La nueva posición para el cuadrado.

        Raises:
        TypeError: Si value no es una tupla de dos enteros positivos.
        """
        firstbool = not all(x >= 0 for x in value)
        secbool = not all(isinstance(x, int) for x in value)
        if (not isinstance(value, tuple) or len(value) != 2 or secbool or firstbool):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

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
        imprime un cuadrado formado por filas y columnas del carácter '#',
        donde el número de filas y columnas es igual al valor de __size,
        precedido por una cantidad de espacios en blanco según la posición.

        Ejemplo:
        Si __size es 3 y __position es (2, 1), el resultado será:

          ###
          ###
          ###

        Si __size es 0, no se imprime nada.
        """
        wsp = 0
        lh = 0
        if self.__size != 0:
            # Imprimir espacios en blanco para la posicion vertical
            while lh < self.__position[1]:
                print()
                lh += 1
            for i in range(self.__size):

                # Imprimir espacios en blanco para la posición horizontal
                while wsp < self.__position[0]:
                    print(' ', end='')
                    wsp += 1
                # Imprimir la fila del cuadrado
                for v in range(self.__size):
                    print('#', end='')
                print()
                wsp = 0
        else:
            print()
