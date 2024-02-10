#!/usr/bin/env python3
"""
N Queens
"""

import sys

if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, i=0, a=[], b=[], c=[]):
    """
    I looks for possible positions
    """
    if i < n:
        for k in range(n):
            if k not in a and i + k not in b and i - k not in c:
                yield from queens(n, i + 1, a + [k], b + [i + k], c + [i - k])
    else:
        yield a


def solve(n):
    """
    Solution
    """
    j = []
    i = 0
    for result in queens(n, 0):
        for s in result:
            j.append([i, s])
            i += 1
        print(j)
        j = []
        i = 0


solve(n)
