import pytest
from .test_utils import load_solution

solution_module = load_solution("0012-Integer-to-Roman.py")
Solution = solution_module.Solution

def test_int_to_roman_example_1():
    sol = Solution()
    assert sol.intToRoman(3) == "III"

def test_int_to_roman_example_2():
    sol = Solution()
    assert sol.intToRoman(4) == "IV"

def test_int_to_roman_example_3():
    sol = Solution()
    assert sol.intToRoman(9) == "IX"

def test_int_to_roman_example_4():
    sol = Solution()
    assert sol.intToRoman(58) == "LVIII"

def test_int_to_roman_example_5():
    sol = Solution()
    assert sol.intToRoman(1994) == "MCMXCIV"

def test_int_to_roman_max():
    sol = Solution()
    assert sol.intToRoman(3999) == "MMMCMXCIX"
