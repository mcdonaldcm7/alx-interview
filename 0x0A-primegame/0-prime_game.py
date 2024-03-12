#!/usr/bin/python3
"""
Tasks: Prime Game
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

    if x <= 0 or nums is None or len(nums) == 0:
        return None

    for i in range(x):
        if primeCountInRange(nums[i]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins == maria_wins:
        return None
    return 'Ben' if ben_wins > maria_wins else 'Maria'
