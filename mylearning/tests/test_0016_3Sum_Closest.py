import pytest
from .test_utils import load_solution

solution_module = load_solution("0016-3Sum-Closest.py")
Solution = solution_module.Solution

def test_3sum_closest_example_1():
    sol = Solution()
    assert sol.threeSumClosest([-1, 2, 1, -4], 1) == 2

def test_3sum_closest_example_2():
    sol = Solution()
    assert sol.threeSumClosest([0, 0, 0], 1) == 0

def test_3sum_closest_large_target():
    sol = Solution()
    assert sol.threeSumClosest([1, 1, 1, 0], -100) == 2

def test_3sum_closest_negative():
    sol = Solution()
    assert sol.threeSumClosest([-1, -1, -1, -1], -2) == -3
