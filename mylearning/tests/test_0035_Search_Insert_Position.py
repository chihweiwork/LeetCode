import pytest
from .test_utils import load_solution

solution_module = load_solution("0035-Search-Insert-Position.py")
Solution = solution_module.Solution

def test_search_insert_example_1():
    sol = Solution()
    assert sol.searchInsert([1, 3, 5, 6], 5) == 2

def test_search_insert_example_2():
    sol = Solution()
    assert sol.searchInsert([1, 3, 5, 6], 2) == 1

def test_search_insert_example_3():
    sol = Solution()
    assert sol.searchInsert([1, 3, 5, 6], 7) == 4

def test_search_insert_example_4():
    sol = Solution()
    assert sol.searchInsert([1, 3, 5, 6], 0) == 0

def test_search_insert_single():
    sol = Solution()
    assert sol.searchInsert([1], 0) == 0
    assert sol.searchInsert([1], 2) == 1
