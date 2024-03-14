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


def isWinner(x, nums):
    """
    Checks and the returns the winner of the most rounds in a Prime Game

    Return: name of the player that won the most rounds
    """
    ben_wins = maria_wins = 0
    if x <= 0:
        return None

    for i in range(x):
        # Sieve of Eratosthenes
        primeNumber = [True for i in range(nums[i] + 1)]
        p = 2

        while (p * p <= nums[i]):
            if (isPrime(p)):
                for num in range(p * p, nums[i] + 1, p):
                    primeNumber[num] = False
            p += 1
        if sum(primeNumber) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins == maria_wins:
        return None
    return 'Ben' if ben_wins > maria_wins else 'Maria'
