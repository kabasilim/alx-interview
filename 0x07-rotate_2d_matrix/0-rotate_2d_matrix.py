#!/usr/bin/python3
"""The rotate_2d_matrix function"""


def rotate_2d_matrix(matrix):
    """The rotate_2d_matrix"""
    dup_matrix = matrix.copy()

    for i in range(0, len(dup_matrix)):
        temp_arr = []
        for j in range(len(dup_matrix) - 1, -1, -1):
            temp_arr.append(dup_matrix[j][i])
        matrix[i] = temp_arr
