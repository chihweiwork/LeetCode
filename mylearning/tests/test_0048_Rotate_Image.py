import pytest
from .test_utils import load_solution

solution_module = load_solution("0048-Rotate-Image.py")
Solution = solution_module.Solution

def test_rotate_example_1():
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol.rotate(matrix)
    assert matrix == [[7,4,1],[8,5,2],[9,6,3]]

def test_rotate_example_2():
    sol = Solution()
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol.rotate(matrix)
    assert matrix == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

def test_rotate_single():
    sol = Solution()
    matrix = [[1]]
    sol.rotate(matrix)
    assert matrix == [[1]]

def test_rotate_2x2():
    sol = Solution()
    matrix = [[1,2],[3,4]]
    sol.rotate(matrix)
    assert matrix == [[3,1],[4,2]]
