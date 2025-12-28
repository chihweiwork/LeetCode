import pytest
from .test_utils import load_solution

solution_module = load_solution("0020-Valid-Parentheses.py")
Solution = solution_module.Solution

def test_is_valid_examples():
    sol = Solution()
    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("([)]") is False
    assert sol.isValid("{[]}") is True

def test_is_valid_empty():
    sol = Solution()
    assert sol.isValid("") is True

def test_is_valid_single():
    sol = Solution()
    assert sol.isValid("(") is False

def test_is_valid_mismatch():
    sol = Solution()
    assert sol.isValid("([)]") is False

def test_is_valid_only_closing():
    sol = Solution()
    assert sol.isValid("]") is False
