#!/usr/bin/python3
"""
Task

0. N queens

The N queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard. Write a program that solves the N queens problem.

     - Usage: nqueens N
        * If the user called the program with the wrong number of arguments,
        print Usage: nqueens N, followed by a new line, and exit with the
        status 1
    - where N must be an integer greater or equal to 4
        * If N is not an integer, print N must be a number, followed by a new
        line, and exit with the status 1
        * If N is smaller than 4, print N must be at least 4, followed by a new
        line, and exit with the status 1
    - The program should print every possible solution to the problem
        * One solution per line
        * You don’t have to print the solutions in a specific order
    - You are only allowed to import the sys module
"""
import sys


if len(sys.argv) <= 1:
    print("Usage: nqueens N")
    exit(1)

n = sys.argv[1]
try:
    n = int(n)
except ValueError:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)

col = set()
posDiag = set()
negDiag = set()

res = []
board = [[0 for i in range(n)] for i in range(n)]


def backtrack(r):
    """
    Uses backtracking to find all possible solutions
    """
    if r == n:
        copy = [row.copy() for row in board]
        res.append(copy)
        return
    for c in range(n):
        if c in col or (r + c) in posDiag or (r - c) in negDiag:
            continue
        col.add(c)
        posDiag.add(r + c)
        negDiag.add(r - c)
        board[r][c] = [r, c]

        backtrack(r + 1)

        col.remove(c)
        posDiag.remove(r + c)
        negDiag.remove(r - c)
        board[r][c] = 0


backtrack(0)
queens = []

for sol in res:
    solution = []
    for row in sol:
        for coord in row:
            if coord != 0:
                solution.append(coord)
    queens.append(solution)

for row in queens:
    print(row)
