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
    factor = []
    i = 2

    # i * i <= n reduces number of iterations required
    while i * i <= n:
        if i in factor:
            i += 1
            continue
        if n % i == 0:
            factor.append(i)

            if n // i != i:
                factor.append(n // i)
        i += 1
    return factor


def minOperations(n: int) -> int:
    """
    Returns fewest number of operations needed to result in exactly `n H`
    characters in the file
    """
    if type(n) != int:
        return 0
    if n <= 1:
        return 0

    fctrs = factors(n)
    non_prime = []
    # Filter factors to ensure only primes are left
    for fct_1 in fctrs:
        for fct_2 in fctrs:
            if fct_1 == fct_2:
                continue
            if (fct_2 % fct_1) == 0:
                non_prime.append(fct_2)
    for non_pr in non_prime:
        if non_pr in fctrs:
            fctrs.remove(non_pr)
    op_count = 0

    if len(fctrs) == 0:
        return n

    while n > 1:
        for fct in fctrs:
            if n % fct == 0:
                n /= fct
                op_count += fct
    return op_count
