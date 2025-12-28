import pytest
from .test_utils import load_solution

solution_module = load_solution("0043-Multiply-Strings.py")
Solution = solution_module.Solution

def test_multiply_example_1():
    sol = Solution()
    assert sol.multiply("2", "3") == "6"

def test_multiply_example_2():
    sol = Solution()
    assert sol.multiply("123", "456") == "56088"

def test_multiply_zero():
    sol = Solution()
    assert sol.multiply("0", "123") == "0"
    assert sol.multiply("123", "0") == "0"

def test_multiply_large():
    sol = Solution()
    assert sol.multiply("999", "999") == "998001"

def test_multiply_one():
    sol = Solution()
    assert sol.multiply("1", "1") == "1"
