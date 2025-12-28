import pytest
from .test_utils import load_solution

solution_module = load_solution("0011-Container-With-Most-Water.py")
Solution = solution_module.Solution

def test_max_area_example():
    sol = Solution()
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

def test_max_area_simple():
    sol = Solution()
    assert sol.maxArea([1, 1]) == 1

def test_max_area_descending():
    sol = Solution()
    assert sol.maxArea([4, 3, 2, 1]) == 4

def test_max_area_u_shape():
    sol = Solution()
    assert sol.maxArea([2, 1, 1, 2]) == 6
