#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates a n by n 2D matrix 90 degrees clockwise in place."""
    n = len(matrix)
    # Check if the matrix is empty or not square
    if n == 0 or any(len(row) != n for row in matrix):
        return

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Flip the matrix horizontally
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
