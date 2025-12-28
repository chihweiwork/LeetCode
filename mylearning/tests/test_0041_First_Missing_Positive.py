import pytest
from .test_utils import load_solution

solution_module = load_solution("0041-First-Missing-Positive.py")
Solution = solution_module.Solution

def test_first_missing_positive_example_1():
    sol = Solution()
    assert sol.firstMissingPositive([1, 2, 0]) == 3

def test_first_missing_positive_example_2():
    sol = Solution()
    assert sol.firstMissingPositive([3, 4, -1, 1]) == 2

def test_first_missing_positive_example_3():
    sol = Solution()
    assert sol.firstMissingPositive([7, 8, 9, 11, 12]) == 1

def test_first_missing_positive_duplicate():
    sol = Solution()
    assert sol.firstMissingPositive([1, 1]) == 2

def test_first_missing_positive_negative():
    sol = Solution()
    assert sol.firstMissingPositive([-5, -10]) == 1

def test_first_missing_positive_consecutive():
    sol = Solution()
    assert sol.firstMissingPositive([1, 2, 3, 4]) == 5
