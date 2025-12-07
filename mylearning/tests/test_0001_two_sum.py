import pytest
from typing import List
from test_utils import load_solution

solution = load_solution("0001-Two-Sum.py")

@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([3, 2, 1, 5], 8, [0, 3]),
])
def test_twoSum(nums: List[int], target: int, expected: List[int]):
    assert sorted(solution.twoSum(nums, target)) == sorted(expected)