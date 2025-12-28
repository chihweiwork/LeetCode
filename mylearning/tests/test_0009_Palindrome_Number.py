import pytest
from .test_utils import load_solution

solution_module = load_solution("0009-Palindrome-Number.py")
Solution = solution_module.Solution

def test_palindrome_example_1():
    sol = Solution()
    assert sol.isPalindrome(121) is True

def test_palindrome_example_2():
    sol = Solution()
    assert sol.isPalindrome(-121) is False

def test_palindrome_example_3():
    sol = Solution()
    assert sol.isPalindrome(10) is False

def test_palindrome_zero():
    sol = Solution()
    assert sol.isPalindrome(0) is True

def test_palindrome_single_digit():
    sol = Solution()
    assert sol.isPalindrome(7) is True

def test_palindrome_even_digits():
    sol = Solution()
    assert sol.isPalindrome(1221) is True
