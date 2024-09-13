#!/usr/bin/python3
"""
This module provides a function `add_integer` that adds two integers.

The function handles both integers and floats, converting floats to integers before performing the addition.

Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats (converted to integers).

    Args:
        a: The first number, must be an integer or float.
        b: The second number, defaults to 98, must be an integer or float.

    Returns:
        The sum of the two numbers as an integer.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    
    a = int(a)
    b = int(b)
    
    return a + b
