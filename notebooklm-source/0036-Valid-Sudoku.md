# 0036 - Valid Sudoku (有效的數獨)

## 1. 題目理解 (Problem Comprehension)

請你判斷一個 9x9 的數獨板是否有效。只需要根據以下規則，驗證已經填入數字的格位：

1.  每一行必須包含數字 `1-9`，且不能重複。
2.  每一列必須包含數字 `1-9`，且不能重複。
3.  每一個 3x3 的九宮格（總共 9 個）也必須包含數字 `1-9`，且不能重複。

**注意：**
*   一個有效的數獨（尚未填滿）不一定是可解的。
*   只需要驗證已經填入的數字是否滿足上述規則。
*   空白格位以 `'.'` 表示。

## 2. 思路分析 (Thought Process)

我們需要檢查三種維度：行、列、九宮格。

**優化思路：一次遍歷 + 哈希集 (Sets)**
我們遍歷整個 9x9 的棋盤一次。對於每個格子 `(r, c)`：
1.  如果它是空的 (`.`)，跳過。
2.  如果它有數字 `val`：
    *   檢查第 `r` 行是否已經出現過 `val`？
    *   檢查第 `c` 列是否已經出現過 `val`？
    *   檢查所在的九宮格是否已經出現過 `val`？

**如何計算九宮格的索引？**
一個 9x9 的棋盤可以分成 9 個 3x3 的九宮格。
索引計算公式為：`box_index = (r // 3) * 3 + (c // 3)`。
*   例如：`(0,0)` 到 `(2,2)` 都在九宮格 0。
*   例如：`(0,3)` 到 `(2,5)` 都在九宮格 1。

我們可以使用 9 個 Set 來儲存每一行看過的數字，9 個 Set 給每一列，9 個 Set 給每個九宮格。

## 3. 演算法設計 (Algorithm Design)

我們採用 **哈希集 (HashSet)** 記錄。

**偽代碼 (Pseudo-code):**

```text
Function isValidSudoku(board):
    Initialize rows = list of 9 empty sets
    Initialize cols = list of 9 empty sets
    Initialize boxes = list of 9 empty sets
    
    For r from 0 to 8:
        For c from 0 to 8:
            val = board[r][c]
            If val == ".": Continue
            
            # 檢查行
            If val in rows[r]: Return False
            rows[r].add(val)
            
            # 檢查列
            If val in cols[c]: Return False
            cols[c].add(val)
            
            # 檢查九宮格
            box_idx = (r // 3) * 3 + (c // 3)
            If val in boxes[box_idx]: Return False
            boxes[box_idx].add(val)
            
    Return True
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(1)**
    *   雖然有嵌套迴圈，但棋盤大小固定為 9x9 = 81 個格子。操作次數是常數。
*   **空間複雜度 (Space Complexity): O(1)**
    *   儲存看過數字的 Set 大小也是固定的（最多 81 個元素）。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 建立 9 個集合來分別儲存每一行、每一列和每個九宮格中出現過的數字
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # 遍歷 9x9 棋盤的每一個格子
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # 如果是空格，則不需要檢查，跳到下一個
                if val == '.':
                    continue
                
                # 1. 檢查目前行是否重複
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                # 2. 檢查目前列是否重複
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                # 3. 檢查目前所在的 3x3 九宮格是否重複
                # box_idx 計算方式：將 9x9 切成 3x3 個大區塊
                # (r // 3) 決定是大區塊的第幾橫排 (0, 1, 2)
                # (c // 3) 決定是大區塊的第幾直排 (0, 1, 2)
                box_idx = (r // 3) * 3 + (c // 3)
                if val in boxes[box_idx]:
                    return False
                boxes[box_idx].add(val)
                
        # 如果所有格子都檢查完畢且沒發現重複，則是有效的數獨
        return True
```
