#!/usr/bin/python3
"""
Implementation of the function 'pascal_triangle'
"""


def pascal_triangle(n):
    """
    Compute and return lists of lists representing the Pascal's triangle of n

    Return: list of lists of integers representing Pascal's triangle of n
    """

    if n == 0:
        return ([])

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
            continue
        curr = []
        prev = triangle[i - 1]
        for j in range(i + 1):
            if j == 0 or j > (len(prev) - 1):
                curr.append(1)
                continue

            idx1 = prev[j - 1]
            idx2 = prev[j]

            curr.append(idx1 + idx2)
        triangle.append(curr)
    return triangle
