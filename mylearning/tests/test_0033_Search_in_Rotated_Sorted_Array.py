import pytest
from .test_utils import load_solution

solution_module = load_solution("0033-Search-in-Rotated-Sorted-Array.py")
Solution = solution_module.Solution

def test_search_rotated_example_1():
    sol = Solution()
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4

def test_search_rotated_example_2():
    sol = Solution()
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1

def test_search_rotated_not_rotated():
    sol = Solution()
    assert sol.search([1, 2, 3], 2) == 1

def test_search_rotated_empty():
    sol = Solution()
    assert sol.search([], 5) == -1

def test_search_rotated_single():
    sol = Solution()
    assert sol.search([1], 1) == 0
    assert sol.search([1], 0) == -1
