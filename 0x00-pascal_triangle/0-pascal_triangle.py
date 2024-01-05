#!/usr/bin/python3
"""The module for pascal triangle
"""


def pascal_triangle(n):
    """This creates a list the stores the binaries for the 
    pascal triangle
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            for k in range(len(last_row) - 1):
                row.append(last_row[k] + last_row[k + 1])
            row.append(1)
        triangle.append(row)
    return triangle
