import pytest
from .test_utils import load_solution

solution_module = load_solution("0017-Letter-Combinations-of-a-Phone-Number.py")
Solution = solution_module.Solution

def test_letter_combinations_example_1():
    sol = Solution()
    result = sol.letterCombinations("23")
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sorted(result) == sorted(expected)

def test_letter_combinations_empty():
    sol = Solution()
    assert sol.letterCombinations("") == []

def test_letter_combinations_single_digit():
    sol = Solution()
    assert sorted(sol.letterCombinations("2")) == ["a", "b", "c"]

def test_letter_combinations_7():
    sol = Solution()
    # 7 has 4 letters
    assert len(sol.letterCombinations("7")) == 4
    assert "p" in sol.letterCombinations("7")
