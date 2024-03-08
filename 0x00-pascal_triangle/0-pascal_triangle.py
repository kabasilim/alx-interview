#!/usr/bin/python3
"""
This file contains the pascal_triangle function
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to level n.

    Args:
    - n: An integer representing the level of Pascal's triangle to generate.

    Returns:
    - A list of lists of integers representing Pascal's triangle.
    - An empty list if n <= 0.
    """
     if n <= 0:
        return []

    triangle = []

    for col in range(n):
        new_row = []
        for row in range(col + 1):
            if row == 0 or col == row:
                new_row.append(1)
            else:
                new_row.append(triangle[col - 1][row] +
                               triangle[col - 1][row - 1])
        triangle.append(new_row)
    return triangle
