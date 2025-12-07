import pytest
import importlib.util
from typing import List

# Load the solution module from the file
spec = importlib.util.spec_from_file_location("solution_0004", "0004-Median-of-Two-Sorted-Arrays.py")
solution_module = importlib.util.module_from_spec(spec)

# The original file is missing `from typing import List`, so we inject it into the module's namespace
solution_module.List = List

spec.loader.exec_module(solution_module)
Solution = solution_module.Solution

@pytest.mark.parametrize("nums1, nums2, expected", [
    ([1, 3], [2], 2.0),
    ([1, 2], [3, 4], 2.5),
    ([0, 0], [0, 0], 0.0),
    ([], [1], 1.0),
    ([2], [], 2.0)
])
def test_findMedianSortedArrays(nums1: List[int], nums2: List[int], expected: float):
    s = Solution()
    assert s.findMedianSortedArrays(nums1, nums2) == expected
