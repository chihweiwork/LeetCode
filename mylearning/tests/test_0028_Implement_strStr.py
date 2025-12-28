import pytest
from .test_utils import load_solution

solution_module = load_solution("0028-Implement-strStr.py")
Solution = solution_module.Solution

def test_str_str_example_1():
    sol = Solution()
    assert sol.strStr("sadbutsad", "sad") == 0

def test_str_str_example_2():
    sol = Solution()
    assert sol.strStr("leetcode", "leeto") == -1

def test_str_str_empty_needle():
    sol = Solution()
    assert sol.strStr("any", "") == 0

def test_str_str_needle_longer():
    sol = Solution()
    assert sol.strStr("abc", "abcd") == -1

def test_str_str_not_found():
    sol = Solution()
    assert sol.strStr("mississippi", "issip") == 4
