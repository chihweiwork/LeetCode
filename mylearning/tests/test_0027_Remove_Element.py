import pytest
from .test_utils import load_solution

solution_module = load_solution("0027-Remove-Element.py")
Solution = solution_module.Solution

def test_remove_element_example_1():
    sol = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    k = sol.removeElement(nums, val)
    assert k == 2
    assert sorted(nums[:k]) == [2, 2]

def test_remove_element_example_2():
    sol = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    k = sol.removeElement(nums, val)
    assert k == 5
    assert sorted(nums[:k]) == sorted([0, 1, 3, 0, 4])

def test_remove_element_empty():
    sol = Solution()
    nums = []
    assert sol.removeElement(nums, 1) == 0

def test_remove_element_all_val():
    sol = Solution()
    nums = [1, 1, 1]
    assert sol.removeElement(nums, 1) == 0

def test_remove_element_none_val():
    sol = Solution()
    nums = [1, 2, 3]
    k = sol.removeElement(nums, 4)
    assert k == 3
    assert sorted(nums[:k]) == [1, 2, 3]
