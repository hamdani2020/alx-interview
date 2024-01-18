#!/usr/bin/python3
"""Alx interview question challenge Minimum operations"""


def minOperations(n):
    """It computes the fewest number of operations needed to
    H characters"""
    if not isinstance(n, int):
        return 0
    O_count = 0
    clipboard_store = 0
    finished = 1
    while finished < n:
        if clipboard_store == 0:
            clipboard_store = finished
            finished += clipboard_store
            O_count += 2
        elif n - finished > 0 and (n - finished) % finished == 0:
            clipboard_store = finished
            finished += clipboard_store
            O_count += 2
        elif clipboard_store > 0:
            finished += clipboard_store
            O_count += 1
    return O_count
