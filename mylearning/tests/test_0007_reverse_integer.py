import pytest
import importlib.util

# Load the solution module from the file
spec = importlib.util.spec_from_file_location("solution_0007", "0007-Reverse-Integer.py")
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
Solution = solution_module.Solution

@pytest.mark.parametrize("x_input, expected", [
    (123, 321),
    (-123, -321),
    (120, 21),
    (0, 0),
    (1534236469, 0),  # This will overflow
    (-2147483648, 0) # This will overflow
])
def test_reverse(x_input: int, expected: int):
    s = Solution()
    assert s.reverse(x_input) == expected
