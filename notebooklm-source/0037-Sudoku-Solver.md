# 0037. Sudoku Solver

```python
# https://leetcode.com/problems/sudoku-solver/
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
#
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for i in range(1, 10):
                        char = str(i)
                        if self.is_valid(board, r, c, char):
                            board[r][c] = char
                            if self.solve(board):
                                return True
                            else:
                                board[r][c] = '.'
                    return False
        return True

    def is_valid(self, board, row, col, char):
        for i in range(9):
            if board[row][i] == char:
                return False
            if board[i][col] == char:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == char:
                return False
        return True

```