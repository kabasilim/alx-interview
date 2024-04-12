#!/usr/bin/python3
"""Defines a solution to the N Queens problem"""
import sys


try:
    N = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    sys.exit(1)
# N = int(sys.argv[1])

"""if not isinstance(N, int):
    print('N must be a number')
    sys.exit(1)"""

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

if N < 4:
    print('N must be at least 4')
    sys.exit(1)


board = []
columns = set()
positive_diag = set()
negative_diag = set()


# create the board positions
for _ in range(N):
    row = [0] * 2
    board.append(row)


def is_safe(r, c):
    """Check if a queen can be placed at position (r, c)"""
    if c in columns or (r + c) in positive_diag or (r - c) in negative_diag:
        return False
    return True


def solve_n_queens(r):
    """recursively places N queens on an N x N chessboard"""
    if r == N:
        print(board)
        return

    for c in range(N):
        if is_safe(r, c):
            columns.add(c)
            positive_diag.add(r + c)
            negative_diag.add(r - c)
            board[r] = [r, c]
            solve_n_queens(r + 1)
            # Backtrack
            columns.remove(c)
            positive_diag.remove(r + c)
            negative_diag.remove(r - c)
            board[r] = [0, 0]


solve_n_queens(0)
