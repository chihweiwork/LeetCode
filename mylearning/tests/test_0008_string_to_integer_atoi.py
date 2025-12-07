import pytest
import importlib.util

# Load the solution module from the file
spec = importlib.util.spec_from_file_location("solution_0008", "0008-String-to-Integer-atoi.py")
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
Solution = solution_module.Solution

@pytest.mark.parametrize("s_input, expected", [
    ("42", 42),
    ("   -42", -42),
    ("4193 with words", 4193),
    ("words and 987", 0),
    ("-91283472332", -2147483648), # INT_MIN
    ("91283472332", 2147483647), # INT_MAX
    ("3.14159", 3),
    ("+1", 1),
    ("+-2", 0),
    ("  0000000000012345678", 12345678),
    (" -10100000000", -2147483648),
    ("", 0),
    (" ", 0)
])
def test_myAtoi(s_input: str, expected: int):
    s = Solution()
    assert s.myAtoi(s_input) == expected
