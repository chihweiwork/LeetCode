import pytest
from importlib.machinery import SourceFileLoader

# 動態從 mylearning 資料夾載入解答模組
solution_module = SourceFileLoader(
    "solution_0009", "mylearning/0009-Palindrome-Number.py"
).load_module()
Solution = solution_module.Solution

@pytest.mark.parametrize("x, expected", [
    (121, True),      # 標準的回文數
    (-121, False),     # 負數不是回文數
    (10, False),       # 結尾是 0 的非零數字不是回文數
    (12321, True),     # 長一點的回文數
    (12345, False),    # 標準的非回文數
    (0, True),         # 0 是回文數
])
def test_isPalindrome(x, expected):
    """
    Test the isPalindrome function with various cases.
    """
    solver = Solution()
    assert solver.isPalindrome(x) == expected
