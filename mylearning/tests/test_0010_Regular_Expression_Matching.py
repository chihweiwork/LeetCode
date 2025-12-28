import pytest
from .test_utils import load_solution

solution_module = load_solution("0010-Regular-Expression-Matching.py")
Solution = solution_module.Solution

def test_regex_example_1():
    sol = Solution()
    assert sol.isMatch("aa", "a") is False

def test_regex_example_2():
    sol = Solution()
    assert sol.isMatch("aa", "a*") is True

def test_regex_example_3():
    sol = Solution()
    assert sol.isMatch("ab", ".*") is True

def test_regex_complex():
    sol = Solution()
    assert sol.isMatch("aab", "c*a*b") is True

def test_regex_no_match():
    sol = Solution()
    assert sol.isMatch("mississippi", "mis*is*p*.") is False

def test_regex_empty():
    sol = Solution()
    assert sol.isMatch("", "") is True
    assert sol.isMatch("", "a*") is True
    assert sol.isMatch("a", "") is False
