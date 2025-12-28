import pytest
from .test_utils import load_solution

solution_module = load_solution("0034-Find-First-and-Last-Position-of-Element-in-Sorted-Array.py")
Solution = solution_module.Solution

def test_search_range_example_1():
    sol = Solution()
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]

def test_search_range_example_2():
    sol = Solution()
    assert sol.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]

def test_search_range_empty():
    sol = Solution()
    assert sol.searchRange([], 0) == [-1, -1]

def test_search_range_all_same():
    sol = Solution()
    assert sol.searchRange([8, 8, 8, 8], 8) == [0, 3]

def test_search_range_single():
    sol = Solution()
    assert sol.searchRange([1], 1) == [0, 0]
