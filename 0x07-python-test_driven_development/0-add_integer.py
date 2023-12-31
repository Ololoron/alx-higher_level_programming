#!/usr/bin/python3
"""Defines a function add_integer(a, b=98) that adds two integers

Attributes
    add_integer: function that adds two integers.
"""


def add_integer(a, b=98):
    """ Adds two integers and/or float values.

    Args:
        a (int): First value
        b (int, optional): Second value. Defaults to 98.
    
    Raises:
        TypeError: If a ans b are not intergers of floats>

    Returns:
        int: Sum of a and b.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b

