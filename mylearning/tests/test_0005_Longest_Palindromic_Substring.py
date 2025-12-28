import pytest
import sys
import os
import importlib.util

# Helper to import module with dashes in name
def load_module(file_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

current_dir = os.path.dirname(os.path.abspath(__file__))
solution_path = os.path.join(current_dir, '..', '0005-Longest-Palindromic-Substring.py')
solution_module = load_module(solution_path, 'solution_0005')
Solution = solution_module.Solution

def test_longest_palindrome_example_1():
    solution = Solution()
    s = "babad"
    result = solution.longestPalindrome(s)
    assert result == "bab" or result == "aba"

def test_longest_palindrome_example_2():
    solution = Solution()
    s = "cbbd"
    result = solution.longestPalindrome(s)
    assert result == "bb"

def test_longest_palindrome_single_char():
    solution = Solution()
    s = "a"
    result = solution.longestPalindrome(s)
    assert result == "a"

def test_longest_palindrome_two_chars():
    solution = Solution()
    s = "ac"
    result = solution.longestPalindrome(s)
    assert result == "a" or result == "c"

def test_longest_palindrome_empty():
    solution = Solution()
    s = ""
    result = solution.longestPalindrome(s)
    assert result == ""

def test_longest_palindrome_all_same():
    solution = Solution()
    s = "aaaa"
    result = solution.longestPalindrome(s)
    assert result == "aaaa"
