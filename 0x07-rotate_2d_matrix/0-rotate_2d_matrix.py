#!/usr/bin/python3
"""
Tasks Rotate 2D Matrix

Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    - Prototype: def rotate_2d_matrix(matrix):
    - Do not return anything. The matrix must be edited in-place.
    - You can assume the matrix will have 2 dimensions and will not be empty
"""


def clockwise_coord(coord, max_n, min_n, n):
    """
    Provides clockwise rotated coordinates
    """
    row = coord[0]
    col = coord[1]

    for i in range(n - 1):
        if row < col:
            # Top/Top-Right Position
            if row == min_n:
                if (col + 1) >= max_n:
                    row += 1
                else:
                    col += 1
            else:
                row += 1
        elif row > col:
            # Bottom/Bottom-Left position
            if col == min_n:
                row -= 1
            else:
                if (col - 1) < min_n:
                    row -= 1
                else:
                    col -= 1
        elif row == col:
            # Square edge
            if row == min_n:
                # Clockwise direction: --->
                col += 1
            else:
                # Clockwise direction: <---
                col -= 1
    return (row, col)


def anticlockwise_coord(coord, max_n, min_n):
    """
    Provides anticlockwise rotated coordinates
    """
    row = coord[0]
    col = coord[1]

    for i in range(max_n - 1):
        if row < col:
            # Top Position
            if (col + 1) >= max_n:
                if (row - 1) < min_n:
                    col -= 1
                else:
                    row -= 1
            else:
                if (col - 1) >= row:
                    col -= 1
                else:
                    row += 1
        elif row > col:
            # Bottom position
            if col == min_n:
                if (row + 1) >= max_n:
                    col += 1
                else:
                    row += 1
            else:
                if (row + 1) >= max_n:
                    col += 1
                else:
                    row += 1
        elif row == col:
            # Square edge
            if row == min_n:
                # Anticlockwise direction: Downward |
                #                                   v
                row += 1
            else:
                # Anticlockwise direction: Upward   ^
                #                                   |
                row -= 1
    return (row, col)


def rotate_2d_matrix(matrix):
    """
    Rotates a 2d matrix
    """
    n = len(matrix)
    i_col = n - 1
    i_row = 0

    for square in range(n//2):
        iter_col = i_col
        for elt in range(n - 1 - square * 2):
            c_row = i_row
            c_col = iter_col
            c_val = matrix[c_row][c_col]
            temp = 0
            for edge in range(4):
                n_iter = n - (square * 2)

                # Replace clockwise_coord with anticlockwise_coor in the line
                # below to rotate in the anticlockwise direction
                coord = clockwise_coord((c_row, c_col), n - square, square,
                                        n_iter)
                n_row = coord[0]
                n_col = coord[1]

                temp = matrix[n_row][n_col]
                matrix[n_row][n_col] = c_val
                c_val = temp

                c_row = n_row
                c_col = n_col
            iter_col -= 1
        i_col -= 1
        i_row += 1
