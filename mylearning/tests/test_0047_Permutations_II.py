import pytest
from .test_utils import load_solution

solution_module = load_solution("0047-Permutations-II.py")
Solution = solution_module.Solution

def test_permute_unique_example_1():
    sol = Solution()
    nums = [1, 1, 2]
    result = sol.permuteUnique(nums)
    expected = [[1,1,2], [1,2,1], [2,1,1]]
    assert sorted(result) == sorted(expected)
    assert len(result) == 3

def test_permute_unique_example_2():
    sol = Solution()
    nums = [1, 2, 3]
    result = sol.permuteUnique(nums)
    assert len(result) == 6

def test_permute_unique_all_same():
    sol = Solution()
    assert sol.permuteUnique([1, 1, 1]) == [[1, 1, 1]]

def test_permute_unique_empty():
    sol = Solution()
    assert sol.permuteUnique([]) == [[]]
