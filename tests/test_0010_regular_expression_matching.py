import pytest
import importlib.util

# Load the solution module from the file
spec = importlib.util.spec_from_file_location("solution_0010", "0010-Regular-Expression-Matching.py")
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
Solution = solution_module.Solution

@pytest.mark.parametrize("s_input, p_input, expected", [
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True),
    ("aab", "c*a*b", True),
    ("mississippi", "mis*is*p*.", False),
    ("", "", True),
    ("a", "", False),
    ("", "a", False),
    ("ab", ".*c", False),
    ("aaa", "a*a", True),
    ("aaa", "ab*a*c*a", True),
])
def test_isMatch(s_input: str, p_input: str, expected: bool):
    s = Solution()
    assert s.isMatch(s_input, p_input) == expected
