#!/usr/bin/python3
"""
Tasks Rotate 2D Matrix

Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    - Prototype: def rotate_2d_matrix(matrix):
    - Do not return anything. The matrix must be edited in-place.
    - You can assume the matrix will have 2 dimensions and will not be empty
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2d matrix
    """
    n = len(matrix)
    i_col = n - 1
    i_row = 0

    for square in range(n//2):
        for elt in range(n):
            c_row = i_row
            c_col = i_col
            temp = False
            for edge in range(4):
                n_row = 0
                n_col = 0
                if edge == 0:
                    n_row = i_row
                    n_col = i_row
                elif edge == 1:
                    n_row = i_col
                    n_col = i_row
                elif edge == 2:
                    n_row = i_col
                    n_col = i_col
                elif edge == 3:
                    n_row = i_row
                    n_col = i_col

                temp = matrix[n_row][n_col]
                matrix[n_row][n_col] = matrix[c_row][c_col]

                # print("Matrix after change on edge {} is:\n{}".format(
                #    edge, matrix))
                # print(
                # "temp: {}\nn_row: {}\nn_col: {}\nc_col: {}\nc_row: {}".format
                # (temp, n_row, n_col, c_col, c_row))

                c_row = n_row
                c_col = n_col
            i_col -= 1
        i_col -= 1
        i_row += 1
