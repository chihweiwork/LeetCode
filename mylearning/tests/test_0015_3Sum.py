import pytest
from .test_utils import load_solution

solution_module = load_solution("0015-3Sum.py")
Solution = solution_module.Solution

def test_3sum_example_1():
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    # Triplets that sum to 0 are [-1, -1, 2] and [-1, 0, 1]
    result = sol.threeSum(nums)
    expected = [[-1, -1, 2], [-1, 0, 1]]
    # Sort for comparison
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])

def test_3sum_example_2():
    sol = Solution()
    nums = [0, 1, 1]
    assert sol.threeSum(nums) == []

def test_3sum_example_3():
    sol = Solution()
    nums = [0, 0, 0]
    assert sol.threeSum(nums) == [[0, 0, 0]]

def test_3sum_empty():
    sol = Solution()
    assert sol.threeSum([]) == []

def test_3sum_no_triplets():
    sol = Solution()
    assert sol.threeSum([1, 2, 3]) == []
