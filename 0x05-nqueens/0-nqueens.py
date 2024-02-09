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

board = [[0 for i in range(n)] for i in range(n)]
row_vacancy = {i: True for i in range(n)}
column_vacancy = {i: True for i in range(n)}
current_row = 0
queen_pos = []

def has_threat(x, y, board):
    """
    Checks whether a square is safe.
    Returns True if it is, Otherwise False
    """
    for i in range(n):
        if (y - i) >= 0 and board[y - i][x] == 1:
            return True
        if (y + i) < n and board[y + i][x] == 1:
            return True
        if (x + i) < n and board[y][x + i] == 1:
            return True
        if (x - i) >= 0 and board[y][x - i] == 1:
            return True
        if (y - i) >= 0 and (x + i) < n and board[y - i][x + i] == 1:
            return True
        if (y - i) >= 0 and (x - i) < n and board[y - i][x - i] == 1:
            return True
        if (y + i) < n and (x + i) < n and board[y + i][x + i] == 1:
            return True
        if (y + i) < n and (x - i) >= 0 and board[y + i][x - i] == 1:
            return True
    return False

def reject(x, y, board):
    """
    Checks whether or not current candidate is a valid solution
    Returns True if it is, Otherwise False
    """
    for y in range(n):
        for x in range(n):
            if board[y][x] != 0:
                if has_threat(x, y, board):
                    return True
    return False

def accept(x ,y, board):
    """
    Checks whether or not current candidate is a complete solution
    Returns True if it is, Otherwise False
    """
    if current_row == (n - 1) and not has_threat(x, y, board):
        return True
    return False

def next_pos(curr_x, curr_y):
    """
    Returns the next valid position for a queen
    """
    if not any(column_vacancy.values()):
        return None

    if curr_x == (n - 1) and curr_y == (n - 1):
        return None

    while row_vacancy[curr_x] == False and column_vacancy[curr_y] == False:
        curr_x += 1
        
        if curr_x == (n - 1):
            if curr_y == (n - 1):
                return None
            curr_x = 0
            curr_y += 1
    return (curr_x, curr_y)


def backtrack(x, y, board, queen_pos, column_vacancy, row_vacancy, current_row = 0):
    """
    """
    if reject(x, y, board):
        return
    if accept(x, y, board):
        print(queen_pos)
    pos = next_pos(x, y)
    next_x = pos[0] if pos is not None else None
    next_y = pos[1] if pos is not None else None
    column_vacancy[next_y] = False if next_y is not None else None
    row_vacancy[next_x] = False if next_x is not None else None
    print("details are next_x: {}, next_y: {}, column_vacancy: {}, row_vacancy\
            : {}, pos: {}".format(next_x, next_y, column_vacancy, row_vacancy, pos))
    if next_y is not None and next_x is not None:
        board[next_y][next_x] = 1

    current_row += 1
    queen_pos.append([next_x, next_y])

    print(board)
    while pos is not None:
        backtrack(next_x, next_y, board, queen_pos, column_vacancy, row_vacancy)
        pos = next_pos(x, y)

backtrack(0, 0, board, queen_pos, column_vacancy, row_vacancy)
