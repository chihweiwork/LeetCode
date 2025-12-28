import pytest
from importlib.machinery import SourceFileLoader
from typing import List

# 動態從 mylearning 資料夾載入解答模組
solution_module = SourceFileLoader(
    "solution_0014", "mylearning/0014-Longest-Common-Prefix.py"
).load_module()
Solution = solution_module.Solution

@pytest.mark.parametrize("strs, expected", [
    (["flower", "flow", "flight"], "fl"),   # 官方範例
    (["dog", "racecar", "car"], ""),        # 沒有共同前綴
    (["apple", "apply", "ape"], "ap"),      # 共同前綴 "ap"
    (["a"], "a"),                           # 只有一個字串
    ([""], ""),                             # 包含空字串
    (["abc", "abc", "abc"], "abc"),         # 所有字串都相同
    ([], ""),                               # 空列表
])
def test_longestCommonPrefix(strs: List[str], expected: str):
    """
    Test the longestCommonPrefix function with various cases.
    """
    solver = Solution()
    assert solver.longestCommonPrefix(strs) == expected
