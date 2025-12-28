import pytest
from importlib.machinery import SourceFileLoader

# 動態從 mylearning 資料夾載入解答模組
solution_module = SourceFileLoader(
    "solution_0012", "mylearning/0012-Integer-to-Roman.py"
).load_module()
Solution = solution_module.Solution

@pytest.mark.parametrize("num, expected", [
    (3, "III"),         # 簡單加法
    (4, "IV"),          # 減法規則
    (9, "IX"),          # 減法規則
    (58, "LVIII"),      # L = 50, V = 5, III = 3
    (1994, "MCMXCIV"),  # 複雜的例子 (M=1000, CM=900, XC=90, IV=4)
    (3999, "MMMCMXCIX") # 最大的可能
])
def test_intToRoman(num, expected):
    """
    Test the intToRoman function with various cases.
    """
    solver = Solution()
    assert solver.intToRoman(num) == expected
