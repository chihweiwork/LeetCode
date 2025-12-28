import pytest
from .test_utils import load_solution

solution_module = load_solution("0030-Substring-with-Concatenation-of-All-Words.py")
Solution = solution_module.Solution

def test_find_substring_example_1():
    sol = Solution()
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    assert sorted(sol.findSubstring(s, words)) == [0, 9]

def test_find_substring_example_2():
    sol = Solution()
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    assert sol.findSubstring(s, words) == []

def test_find_substring_example_3():
    sol = Solution()
    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    assert sorted(sol.findSubstring(s, words)) == [6, 9, 12]

def test_find_substring_empty():
    sol = Solution()
    assert sol.findSubstring("", ["a"]) == []
    assert sol.findSubstring("a", []) == []

def test_find_substring_overlap():
    sol = Solution()
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    # "word" + "good" + "best" + "good"
    assert sorted(sol.findSubstring(s, words)) == [8]
