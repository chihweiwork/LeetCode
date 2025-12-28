import pytest
from .test_utils import load_solution

solution_module = load_solution("0026-Remove-Duplicates-from-Sorted-Array.py")
Solution = solution_module.Solution

def test_remove_duplicates_example_1():
    sol = Solution()
    nums = [1, 1, 2]
    k = sol.removeDuplicates(nums)
    assert k == 2
    assert nums[:k] == [1, 2]

def test_remove_duplicates_example_2():
    sol = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = sol.removeDuplicates(nums)
    assert k == 5
    assert nums[:k] == [0, 1, 2, 3, 4]

def test_remove_duplicates_empty():
    sol = Solution()
    nums = []
    assert sol.removeDuplicates(nums) == 0

def test_remove_duplicates_no_duplicates():
    sol = Solution()
    nums = [1, 2, 3]
    k = sol.removeDuplicates(nums)
    assert k == 3
    assert nums[:k] == [1, 2, 3]
