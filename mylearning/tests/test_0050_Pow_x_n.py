import pytest
from .test_utils import load_solution

solution_module = load_solution("0050-Pow-x-n.py")
Solution = solution_module.Solution

def test_pow_example_1():
    sol = Solution()
    assert abs(sol.myPow(2.00000, 10) - 1024.00000) < 1e-5

def test_pow_example_2():
    sol = Solution()
    assert abs(sol.myPow(2.10000, 3) - 9.26100) < 1e-5

def test_pow_example_3():
    sol = Solution()
    assert abs(sol.myPow(2.00000, -2) - 0.25000) < 1e-5

def test_pow_zero_exponent():
    sol = Solution()
    assert sol.myPow(5.0, 0) == 1.0

def test_pow_zero_base():
    sol = Solution()
    assert sol.myPow(0.0, 5) == 0.0

def test_pow_one_base():
    sol = Solution()
    assert sol.myPow(1.0, 100) == 1.0
