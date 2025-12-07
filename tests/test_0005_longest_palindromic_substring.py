import pytest
import importlib.util

# Load the solution module from the file
spec = importlib.util.spec_from_file_location("solution_0005", "0005-Longest-Palindromic-Substring.py")
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
Solution = solution_module.Solution

@pytest.mark.parametrize("s_input, expected", [
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("a", "a"),
    ("ac", "a"),
    ("racecar", "racecar"),
    (" ", " "),
    ("", "")
])
def test_longestPalindrome(s_input: str, expected: str):
    s = Solution()
    assert s.longestPalindrome(s_input) == expected
