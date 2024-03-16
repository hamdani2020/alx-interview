#!/usr/bin/python3
""" Module for the Prime Game"""


def isWinner(x, nums):
    """x - rounds
    num - numbers list
    """
    if x <= 0 or num is None:
        return None
    if x != len(num):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(num)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in num:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """ It removes multiple primes
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break