import pytest
from .test_utils import load_solution

solution_module = load_solution("0039-Combination-Sum.py")
Solution = solution_module.Solution

def test_combination_sum_example_1():
    sol = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    expected = [[2, 2, 3], [7]]
    result = sol.combinationSum(candidates, target)
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])

def test_combination_sum_example_2():
    sol = Solution()
    candidates = [2, 3, 5]
    target = 8
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    result = sol.combinationSum(candidates, target)
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])

def test_combination_sum_empty():
    sol = Solution()
    assert sol.combinationSum([2], 1) == []

def test_combination_sum_single():
    sol = Solution()
    assert sol.combinationSum([1], 1) == [[1]]
