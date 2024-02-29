#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    It returns the minimum number of coins
    """
    if total <= 0:
        return 0
    reminder = total
    coins_count = 0
    coins_idx = 0
    sort_coins = sorted(coins, reverse=True)
    n = len(coins)
    while reminder > 0:
        if coins_idx >= n:
            return -1
        if reminder - sort_coins[coins_idx] >= 0:
            reminder -= sort_coins[coins_idx]
            coins_count += 1
        else:
            coins_idx += 1
    return coins_count
