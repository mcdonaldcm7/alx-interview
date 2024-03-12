#!/usr/bin/python3
"""
Tasks

0. Prime Game

Maria and Ben are playing a game. Given a set of consecutive integers starting
from 1 up to and including n, they take turns choosing a prime number from the
set and removing that number and its multiples from the set. The player that
cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally, determine who
the winner of each game is.

    - Prototype: def isWinner(x, nums)
    - where x is the number of rounds and nums is an array of n
    - Return: name of the player that won the most rounds
    - If the winner cannot be determined, return None
    - You can assume n and x will not be larger than 10000
    - You cannot import any packages in this task
"""


def isPrime(n):
    """
    Checks if a number is prime

    Return: True if n is a prime number, Otherwise False
    """
    if (n <= 1):
        return False
    i = 2
    while (i * i) <= n:
        if (n % i) == 0:
            return False
        i += 1
    return True


def primeCountInRange(n):
    """
    Computes the number of prime numbers in the given range n

    Return: Number of prime number's between 1 and n
    """
    primeCount = 0
    for i in range(2, n + 1):
        if isPrime(i):
            primeCount += 1
    return primeCount


def isWinner(x, nums):
    """
    Checks and the returns the winner of the most rounds in a Prime Game

    Return: name of the player that won the most rounds
    """
    ben_wins = maria_wins = 0

    if x <= 0:
        return None

    for i in range(x):
        if primeCountInRange(nums[i]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins == maria_wins:
        return None
    return 'Ben' if ben_wins > maria_wins else 'Maria'
