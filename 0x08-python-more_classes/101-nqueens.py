#!/usr/bin/python3
"""Solves the N-queens puzzle."""
import sys


def init_tableau(n):
    """Initialize an NxN sized chessboard with 0's."""
    tableau = []
    [tableau.append([]) for a in range(n)]
    [r.append(' ') for a in range(n) for r in tableau]
    return (tableau)


def tableau_deepcopy(table):
    """Return a deepcopy of a chessboard."""
    if isinstance(table, list):
        return list(map(tableau_deepcopy, table))
    return (table)


def get_solution(table):
    """Return the list of lists representation of a solved chessboard."""
    sol = []
    for a in range(len(table)):
        for b in range(len(table)):
            if table[a][b] == "Q":
                sol.append([a, b])
                break
    return (sol)


def xout(table, row, col):
    """X out spots on a chessboard."""
    # X out all forward spots
    for a in range(col + 1, len(table)):
        table[row][a] = "x"
    # X out all backwards spots
    for a in range(col - 1, -1, -1):
        table[row][a] = "x"
    # X out all spots below
    for r in range(row + 1, len(table)):
        table[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        table[r][col] = "x"
    # X out all spots diagonally down to the right
    a = col + 1
    for r in range(row + 1, len(table)):
        if a >= len(table):
            break
        table[r][a] = "x"
        a += 1
    # X out all spots diagonally up to the left
    a = col - 1
    for r in range(row - 1, -1, -1):
        if a < 0:
            break
        table[r][a]
        a -= 1
    # X out all spots diagonally up to the right
    a = col + 1
    for r in range(row - 1, -1, -1):
        if a >= len(table):
            break
        table[r][a] = "x"
        a += 1
    # X out all spots diagonally down to the left
    a = col - 1
    for r in range(row + 1, len(table)):
        if a < 0:
            break
        table[r][a] = "x"
        a -= 1


def recursive_solve(table, row, queens, sol):
    """Recursively solve an N-queens puzzle."""
    if queens == len(table):
        sol.append(get_solution(table))
        return (sol)

    for a in range(len(table)):
        if table[row][a] == " ":
            tmp_board = tableau_deepcopy(table)
            tmp_board[row][a] = "Q"
            xout(tmp_board, row, a)
            sol = recursive_solve(tmp_board, row + 1,
                                        queens + 1, sol)

    return (sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    table = init_tableau(int(sys.argv[1]))
    solution = recursive_solve(table, 0, 0, [])
    for sol in solution:
        print(sol)
