import pytest
from .test_utils import load_solution

solution_module = load_solution("0032-Longest-Valid-Parentheses.py")
Solution = solution_module.Solution

def test_longest_valid_example_1():
    sol = Solution()
    assert sol.longestValidParentheses("(()") == 2

def test_longest_valid_example_2():
    sol = Solution()
    assert sol.longestValidParentheses(")()())") == 4

def test_longest_valid_empty():
    sol = Solution()
    assert sol.longestValidParentheses("") == 0

def test_longest_valid_nested():
    sol = Solution()
    assert sol.longestValidParentheses("((()))") == 6

def test_longest_valid_mixed():
    sol = Solution()
    assert sol.longestValidParentheses("()(()))))") == 6
