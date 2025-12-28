import pytest
from .test_utils import load_solution

solution_module = load_solution("0022-Generate-Parentheses.py")
Solution = solution_module.Solution

def test_generate_parentheses_example():
    sol = Solution()
    result = sol.generateParenthesis(3)
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sorted(result) == sorted(expected)

def test_generate_parentheses_n1():
    sol = Solution()
    assert sol.generateParenthesis(1) == ["()"]

def test_generate_parentheses_n2():
    sol = Solution()
    assert sorted(sol.generateParenthesis(2)) == sorted(["(())", "()()"])
