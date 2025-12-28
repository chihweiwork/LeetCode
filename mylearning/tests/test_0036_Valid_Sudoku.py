import pytest
from .test_utils import load_solution

solution_module = load_solution("0036-Valid-Sudoku.py")
Solution = solution_module.Solution

def test_is_valid_sudoku_example_1():
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    assert sol.isValidSudoku(board) is True

def test_is_valid_sudoku_example_2():
    sol = Solution()
    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    # Same as example 1 but the top-left '5' is replaced by '8'
    # Row 0 has two '8's (at [0,0] and [0,4] is '.' but wait, there's another '8' in col 0)
    # Actually, in this case, Col 0 has two '8's (at [0,0] and [3,0])
    assert sol.isValidSudoku(board) is False
