import pytest
import importlib.util

# Load the solution module from the file
spec = importlib.util.spec_from_file_location("solution_0006", "0006-ZigZag-Conversion.py")
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
Solution = solution_module.Solution

@pytest.mark.parametrize("s_input, num_rows, expected", [
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ("A", 1, "A"),
    ("AB", 1, "AB"),
    ("ABCDE", 4, "ABCED")
])
def test_convert(s_input: str, num_rows: int, expected: str):
    s = Solution()
    assert s.convert(s_input, num_rows) == expected
