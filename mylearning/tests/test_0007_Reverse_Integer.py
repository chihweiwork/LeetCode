import pytest
from .test_utils import load_solution

solution_module = load_solution("0007-Reverse-Integer.py")
Solution = solution_module.Solution

def test_reverse_positive():
    sol = Solution()
    assert sol.reverse(123) == 321

def test_reverse_negative():
    sol = Solution()
    assert sol.reverse(-123) == -321

def test_reverse_with_zero():
    sol = Solution()
    assert sol.reverse(120) == 21

def test_reverse_zero():
    sol = Solution()
    assert sol.reverse(0) == 0

def test_reverse_overflow():
    sol = Solution()
    # 1534236469 reversed would exceed 32-bit int
    assert sol.reverse(1534236469) == 0
