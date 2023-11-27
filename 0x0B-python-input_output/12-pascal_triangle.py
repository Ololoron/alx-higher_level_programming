#!/usr/bin/python3
"""Module containing the function pascal_triangle
"""


def pascal_triangle(n):
    """Returns a list of list of integers representiong the Pascal's
    triangle of n

    Args:
        n (list): rows of triangle.

    Returns:
        list: list of lists of integers.
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    pascal = [[1]]
    for i in range(n - 1):
        pascal.append([x + n for x, n in zip(pascal[-1] + [0],
                                             [0] + pascal[-1])])
    return (pascal)
