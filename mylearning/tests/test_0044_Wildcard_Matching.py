import pytest
from .test_utils import load_solution

solution_module = load_solution("0044-Wildcard-Matching.py")
Solution = solution_module.Solution

def test_wildcard_example_1():
    sol = Solution()
    assert sol.isMatch("aa", "a") is False

def test_wildcard_example_2():
    sol = Solution()
    assert sol.isMatch("aa", "*") is True

def test_wildcard_example_3():
    sol = Solution()
    assert sol.isMatch("cb", "?a") is False

def test_wildcard_star_complex():
    sol = Solution()
    assert sol.isMatch("adceb", "*a*b") is True

def test_wildcard_mismatch():
    sol = Solution()
    assert sol.isMatch("acdcb", "a*c?b") is False

def test_wildcard_empty():
    sol = Solution()
    assert sol.isMatch("", "") is True
    assert sol.isMatch("", "*") is True
    assert sol.isMatch("a", "") is False
