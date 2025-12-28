import pytest
from .test_utils import load_solution

solution_module = load_solution("0049-Group-Anagrams.py")
Solution = solution_module.Solution

def test_group_anagrams_example_1():
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    result = sol.groupAnagrams(strs)
    # Convert inner lists to sorted tuples for easy comparison
    actual = sorted([sorted(x) for x in result])
    expected = sorted([sorted(["bat"]), sorted(["nat","tan"]), sorted(["ate","eat","tea"])])
    assert actual == expected

def test_group_anagrams_empty():
    sol = Solution()
    assert sol.groupAnagrams([""]) == [[""]]

def test_group_anagrams_single():
    sol = Solution()
    assert sol.groupAnagrams(["a"]) == [["a"]]

def test_group_anagrams_all_different():
    sol = Solution()
    strs = ["abc", "def", "ghi"]
    result = sol.groupAnagrams(strs)
    assert len(result) == 3
