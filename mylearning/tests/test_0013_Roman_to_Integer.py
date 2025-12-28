import pytest
from .test_utils import load_solution

solution_module = load_solution("0013-Roman-to-Integer.py")
Solution = solution_module.Solution

def test_roman_to_int_example_1():
    sol = Solution()
    assert sol.romanToInt("III") == 3

def test_roman_to_int_example_2():
    sol = Solution()
    assert sol.romanToInt("IV") == 4

def test_roman_to_int_example_3():
    sol = Solution()
    assert sol.romanToInt("IX") == 9

def test_roman_to_int_example_4():
    sol = Solution()
    assert sol.romanToInt("LVIII") == 58

def test_roman_to_int_example_5():
    sol = Solution()
    assert sol.romanToInt("MCMXCIV") == 1994

def test_roman_to_int_max():
    sol = Solution()
    assert sol.romanToInt("MMMCMXCIX") == 3999
