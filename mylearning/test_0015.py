import pytest
from importlib.machinery import SourceFileLoader
from typing import List

# 動態從 mylearning 資料夾載入解答模組
solution_module = SourceFileLoader(
    "solution_0015", "mylearning/0015-3Sum.py"
).load_module()
Solution = solution_module.Solution

def sort_list_of_lists(list_of_lists: List[List[int]]) -> List[List[int]]:
    """Helper function to sort lists of lists to make them comparable."""
    return sorted([sorted(sublist) for sublist in list_of_lists])

@pytest.mark.parametrize("nums, expected", [
    (
        [-1, 0, 1, 2, -1, -4],
        [[-1, -1, 2], [-1, 0, 1]]
    ),
    (
        [],
        []
    ),
    (
        [0],
        []
    ),
    (
        [0, 0, 0, 0],
        [[0, 0, 0]]
    ),
    (
        [-2, 0, 1, 1, 2],
        [[-2, 0, 2], [-2, 1, 1]]
    ),
])
def test_threeSum(nums: List[int], expected: List[List[int]]):
    """
    Test the threeSum function.
    The order of the triplets and the order of elements within triplets
    does not matter, so we sort both the actual and expected results
    before comparison to ensure the test is robust.
    """
    solver = Solution()
    actual = solver.threeSum(nums)
    
    # Sort for comparison
    sorted_actual = sort_list_of_lists(actual)
    sorted_expected = sort_list_of_lists(expected)
    
    assert sorted_actual == sorted_expected
