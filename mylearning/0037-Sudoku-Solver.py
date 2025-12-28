from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self._solve(board)

    def _solve(self, board: List[List[str]]) -> bool:
        # Find the next empty cell
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    # Try digits 1-9
                    for num in "123456789":
                        if self._is_valid(board, r, c, num):
                            # Make a choice
                            board[r][c] = num
                            
                            # Recursively try to solve the rest
                            if self._solve(board):
                                return True
                            
                            # Backtrack: undo the choice
                            board[r][c] = '.'
                    
                    # If no digit works, this branch is invalid
                    return False
        
        # All cells filled correctly
        return True

    def _is_valid(self, board: List[List[str]], row: int, col: int, char: str) -> bool:
        for i in range(9):
            # Check row
            if board[row][i] == char:
                return False
            # Check column
            if board[i][col] == char:
                return False
            # Check 3x3 box
            # Formula for box traversal:
            # row starts at (row // 3) * 3, col starts at (col // 3) * 3
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == char:
                return False
        return True
