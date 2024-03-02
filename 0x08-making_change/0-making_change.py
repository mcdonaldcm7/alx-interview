#!/usr/bin/python3
"""
Tasks

0. Change comes from within

Given a pile of coins of different values, determine the fewest number of coins
needed to meet a given amount total.

    - Prototype: def makeChange(coins, total)
    - Return: fewest number of coins needed to meet total
        * If total is 0 or less, return 0
        * If total cannot be met by any number of coins you have, return -1
    - coins is a list of the values of the coins in your possession
    - The value of a coin will always be an integer greater than 0
    - You can assume you have an infinite number of each denomination of coin
    in the list
    - Your solution’s runtime will be evaluated in this task

Test:

carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
\"\"\"
Main file for testing
\"\"\"

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$

Expected Output:
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$
"""


def makeChange(coins, total):
    """
    Returns fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    for i in range(len(coins)):
        cut = 0
        tmp_total = total
        for coin in coins[i:]:
            if coin > tmp_total:
                continue
            cut += tmp_total // coin
            if tmp_total % coin == 0:
                return cut
            tmp_total -= coin * (tmp_total // coin)
    return -1
