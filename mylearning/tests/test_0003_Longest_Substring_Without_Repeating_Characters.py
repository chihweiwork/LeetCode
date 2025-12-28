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
solution_path = os.path.join(current_dir, '..', '0003-Longest-Substring-Without-Repeating-Characters.py')
solution_module = load_module(solution_path, 'solution_0003')
Solution = solution_module.Solution

def test_length_of_longest_substring_example_1():
    solution = Solution()
    s = "abcabcbb"
    expected = 3
    assert solution.lengthOfLongestSubstring(s) == expected

def test_length_of_longest_substring_example_2():
    solution = Solution()
    s = "bbbbb"
    expected = 1
    assert solution.lengthOfLongestSubstring(s) == expected

def test_length_of_longest_substring_example_3():
    solution = Solution()
    s = "pwwkew"
    expected = 3
    assert solution.lengthOfLongestSubstring(s) == expected

def test_length_of_longest_substring_empty():
    solution = Solution()
    s = ""
    expected = 0
    assert solution.lengthOfLongestSubstring(s) == expected

def test_length_of_longest_substring_space():
    solution = Solution()
    s = " "
    expected = 1
    assert solution.lengthOfLongestSubstring(s) == expected

def test_length_of_longest_substring_abba():
    solution = Solution()
    s = "abba"
    expected = 2
    assert solution.lengthOfLongestSubstring(s) == expected
