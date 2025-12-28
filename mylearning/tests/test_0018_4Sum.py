import pytest
from .test_utils import load_solution

solution_module = load_solution("0018-4Sum.py")
Solution = solution_module.Solution

def test_4sum_example_1():
    sol = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    # Expected: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    result = sol.fourSum(nums, target)
    expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])

def test_4sum_example_2():
    sol = Solution()
    nums = [2, 2, 2, 2, 2]
    target = 8
    assert sol.fourSum(nums, target) == [[2, 2, 2, 2]]

def test_4sum_no_solution():
    sol = Solution()
    assert sol.fourSum([1, 2, 3], 6) == []
