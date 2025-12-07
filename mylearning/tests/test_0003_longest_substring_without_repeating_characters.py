import pytest
import importlib.util

# Load the solution module from the file
spec = importlib.util.spec_from_file_location("solution_0003", "0003-Longest-Substring-Without-Repeating-Characters.py")
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
Solution = solution_module.Solution

@pytest.mark.parametrize("s_input, expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    (" ", 1),
    ("", 0),
    ("au", 2),
    ("dvdf", 3),
    ("nishant", 6)
])
def test_lengthOfLongestSubstring(s_input: str, expected: int):
    s = Solution()
    assert s.lengthOfLongestSubstring(s_input) == expected
