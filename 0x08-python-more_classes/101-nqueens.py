#!/usr/bin/python3

"""This module contains the solution for the challenge"""

import sys


def is_safe(chessboard, row, column):
    """
    Check if a queen can be placed on board[row][col]

    Arguments:
        chessboard:
            is the current state of the chessboard
        row:
            is the row to check
        column:
            is the column to check

    Returns:
        True if a queen can be placed at (row, col), False otherwise

    """

    for i in range(column):
        if chessboard[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if chessboard[i][j] == 1:
            return False

    for i, j in zip(range(row, len(chessboard)), range(column, -1, -1)):
        if chessboard[i][j] == 1:
            return False

    return True


def solve_nqueens(chessboard, column, results):
    """
    Solve the N queens problem recursively.

    Args:
        chessboard: The N x N chessboard represented as a 2D list.
        column: The current column being processed.
        results: A list to store the valid results.

    Returns:
        True if a result is found, False otherwise.

    """
    N = len(chessboard)

    if column == N:
        result = [[i, j] for i in range(
            N)for j in range(N) if chessboard[i][j] == 1]
        results.append(result)
        return True

    for row in range(N):
        if is_safe(chessboard, row, column):
            chessboard[row][column] = 1
            solve_nqueens(chessboard, column + 1, results)
            chessboard[row][column] = 0


def print_solutions(results):
    """
    Print all results

    Args:
        results (list): List of results to be printed

    """
    for result in results:
        print(result)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = [[0] * N for _ in range(N)]
    results = []
    solve_nqueens(chessboard, 0, results)
    print_solutions(results)
