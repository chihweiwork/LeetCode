import pytest
from importlib.machinery import SourceFileLoader

# 動態從 mylearning 資料夾載入解答模組
solution_module = SourceFileLoader(
    "solution_0011", "mylearning/0011-Container-With-Most-Water.py"
).load_module()
Solution = solution_module.Solution

@pytest.mark.parametrize("height, expected", [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),  # LeetCode 官方範例
    ([1, 1], 1),                      # 最簡單的情況
    ([4, 3, 2, 1, 4], 16),             # 兩端一樣高
    ([1, 2, 1], 2),                      # 中間比較高
    ([2, 3, 10, 5, 7, 8, 9], 36)      # 複雜一點的例子
])
def test_maxArea(height, expected):
    """
    Test the maxArea function with various cases.
    """
    solver = Solution()
    assert solver.maxArea(height) == expected
