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

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
