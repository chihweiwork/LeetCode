import pytest
import importlib.util

# Load the solution module from the file
spec = importlib.util.spec_from_file_location("solution_0009", "0009-Palindrome-Number.py")
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
Solution = solution_module.Solution

@pytest.mark.parametrize("x_input, expected", [
    (121, True),
    (-121, False),
    (10, False),
    (0, True),
    (1, True),
    (11, True),
    (12321, True),
    (12345, False)
])
def test_isPalindrome(x_input: int, expected: bool):
    s = Solution()
    assert s.isPalindrome(x_input) == expected
