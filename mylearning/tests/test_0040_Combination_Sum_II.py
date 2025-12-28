import pytest
from .test_utils import load_solution

solution_module = load_solution("0040-Combination-Sum-II.py")
Solution = solution_module.Solution

def test_combination_sum2_example_1():
    sol = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    result = sol.combinationSum2(candidates, target)
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])

def test_combination_sum2_example_2():
    sol = Solution()
    candidates = [2, 5, 2, 1, 2]
    target = 5
    expected = [[1, 2, 2], [5]]
    result = sol.combinationSum2(candidates, target)
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])

def test_combination_sum2_no_solution():
    sol = Solution()
    assert sol.combinationSum2([2], 1) == []

def test_combination_sum2_all_same():
    sol = Solution()
    assert sol.combinationSum2([1, 1, 1], 2) == [[1, 1]]
