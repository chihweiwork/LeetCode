import pytest
from .test_utils import load_solution

solution_module = load_solution("0008-String-to-Integer-atoi.py")
Solution = solution_module.Solution

def test_atoi_example_1():
    sol = Solution()
    assert sol.myAtoi("42") == 42

def test_atoi_example_2():
    sol = Solution()
    assert sol.myAtoi("   -42") == -42

def test_atoi_example_3():
    sol = Solution()
    assert sol.myAtoi("4193 with words") == 4193

def test_atoi_words_first():
    sol = Solution()
    assert sol.myAtoi("words and 987") == 0

def test_atoi_overflow():
    sol = Solution()
    assert sol.myAtoi("-91283472332") == -2147483648

def test_atoi_plus_minus():
    sol = Solution()
    assert sol.myAtoi("+-12") == 0

def test_atoi_empty():
    sol = Solution()
    assert sol.myAtoi("") == 0
