#!/usr/bin/python3
"""solves the N-queens puzzle"""
import sys


def init_board(n):
    """Initialize an NxN sized chessboard with 0's."""
    board = []
    [board.append([]) for a in range(n)]
    [row.append(' ') for a in range(n) for row in board]
    return (board)

def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    sol = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                sol.append([r, c])
                break
    return (sol)

def xout(board, row, col):
    """X out spots on a chessboard."""
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1

def recursive_solve(board, row, queens, solu):
    """Recursively solve an N-queens puzzle."""
    if queens == len(board):
        solu.append(get_solution(board))
        return (solu)

    for b in range(len(board)):
        if board[row][b] == " ":
            temp_board = board_deepcopy(board)
            temp_board[row][b] = "Q"
            xout(temp_board, row, b)
            solu = recursive_solve(temp_board, row + 1, queens + 1, solu)
    return (solu)

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

    board = init_board(int(sys.argv[1]))
    solu = recursive_solve(board, 0, 0, [])
    for sol in solu:
        print(sol)
