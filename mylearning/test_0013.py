import pytest
from importlib.machinery import SourceFileLoader

# 動態從 mylearning 資料夾載入解答模組
solution_module = SourceFileLoader(
    "solution_0013", "mylearning/0013-Roman-to-Integer.py"
).load_module()
Solution = solution_module.Solution

@pytest.mark.parametrize("s, expected", [
    ("III", 3),
    ("IV", 4),
    ("IX", 9),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
    ("MMMCMXCIX", 3999),
])
def test_romanToInt(s, expected):
    """
    Test the romanToInt function with various cases.
    """
    solver = Solution()
    assert solver.romanToInt(s) == expected
