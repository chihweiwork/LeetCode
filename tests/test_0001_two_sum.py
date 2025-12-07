import pytest
import importlib.util
from typing import List

# Load the solution module from the file
# The file path is relative to the root of the project, where pytest is run.
spec = importlib.util.spec_from_file_location("solution_0001", "0001-Two-Sum.py")
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
Solution = solution_module.Solution

@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([3, 2, 1, 5], 8, [0, 3]),
])
def test_twoSum(nums: List[int], target: int, expected: List[int]):
    s = Solution()
    assert sorted(s.twoSum(nums, target)) == sorted(expected)
