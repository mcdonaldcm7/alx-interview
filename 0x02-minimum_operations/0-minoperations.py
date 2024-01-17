#!/usr/bin/python3
"""
Task

0. Minimum Operations

In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write a
method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.

    - Prototype: def minOperations(n)
    - Returns an integer
    - If n is impossible to achieve, return 0

Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH =>
Paste => HHHHHHHHH

Number of operations: 6
"""
from typing import List
import math


def factors(n: int) -> List[int]:
    """
    Returns a list of the numbers that divide n
    """
    factors = []
    i = 2
    # for i in range(2, math.ceil(n / 2) + 1):
    #    if (i != n) and (n % i) == 0:
    #        factors.append(i)
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            if n // i != i:
                factors.append(n // i)
        i += 1
    return factors


def minOperations(n: int) -> int:
    """
    Returns fewest number of operations needed to result in exactly `n H`
    characters in the file
    """
    fctrs = factors(n)
    text = 'H'
    copied = 'H'
    op_count = 1
    if type(n) != int or n <= 1:
        return 0
    if len(fctrs) == 0:
        return n
    while len(text) < n:
        if len(text) in fctrs:
            copied = text
            op_count += 1
        text += copied
        op_count += 1
    return op_count
