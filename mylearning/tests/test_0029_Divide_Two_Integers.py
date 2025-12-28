import pytest
from .test_utils import load_solution

solution_module = load_solution("0029-Divide-Two-Integers.py")
Solution = solution_module.Solution

def test_divide_example_1():
    sol = Solution()
    assert sol.divide(10, 3) == 3

def test_divide_example_2():
    sol = Solution()
    assert sol.divide(7, -3) == -2

def test_divide_zero_dividend():
    sol = Solution()
    assert sol.divide(0, 1) == 0

def test_divide_overflow():
    sol = Solution()
    # -2147483648 / -1 = 2147483648, which overflows to 2147483647
    assert sol.divide(-2147483648, -1) == 2147483647

def test_divide_same_value():
    sol = Solution()
    assert sol.divide(100, 100) == 1
    assert sol.divide(100, -100) == -1
