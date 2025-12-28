import pytest
from .test_utils import load_solution

solution_module = load_solution("0014-Longest-Common-Prefix.py")
Solution = solution_module.Solution

def test_lcp_example_1():
    sol = Solution()
    assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"

def test_lcp_example_2():
    sol = Solution()
    assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""

def test_lcp_single_word():
    sol = Solution()
    assert sol.longestCommonPrefix(["apple"]) == "apple"

def test_lcp_empty_list():
    sol = Solution()
    assert sol.longestCommonPrefix([]) == ""

def test_lcp_one_empty_string():
    sol = Solution()
    assert sol.longestCommonPrefix(["", "b"]) == ""

def test_lcp_all_same():
    sol = Solution()
    assert sol.longestCommonPrefix(["test", "test", "test"]) == "test"
