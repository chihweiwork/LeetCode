# 0037 - Sudoku Solver (解數獨)

## 1. 題目理解 (Problem Comprehension)

編寫一個程式，透過填充空白格位來解決數獨問題。

一個數獨的解法需遵循以下規則：
1.  數字 `1-9` 在每一行只能出現一次。
2.  數字 `1-9` 在每一列只能出現一次。
3.  數字 `1-9` 在每一個以粗實線分隔的 3x3 九宮格內只能出現一次。

空白格位用 `'.'` 表示。

這是一道 LeetCode 的 **Hard** 題目。

**輸入與輸出格式：**
*   **輸入 (Input):** `board`: 9x9 的字串二維列表。
*   **輸出 (Output):** 無（直接修改 `board`）。

## 2. 思路分析 (Thought Process)

這是一個經典的搜索問題。我們需要填滿所有的空白格，且每一步的選擇都要滿足數獨規則。

**優化思路：回溯演算法 (Backtracking)**
回溯法是一種「試錯」的搜尋策略：
1.  **尋找空格**：找到棋盤上第一個還沒填數字的地方。
2.  **嘗試填入**：依序嘗試填入 `1` 到 `9`。
3.  **合法性檢查**：在填入某個數字前，檢查它是否與目前的行、列、九宮格衝突。
4.  **繼續搜尋**：如果填入合法，就遞迴地去解剩下的棋盤。
5.  **撤銷 (Backtrack)**：如果後面的棋盤解不出來（返回 False），代表目前這個數字選錯了。我們將目前格子恢復成 `'.'`，並嘗試下一個數字。
6.  **完成**：當沒有空格時，代表解題成功。

## 3. 演算法設計 (Algorithm Design)

我們採用 **深度優先搜尋 (DFS) / 回溯法**。

**偽代碼 (Pseudo-code):**

```text
Function solve(board):
    For each cell (r, c) in board:
        If board[r][c] == ".":
            For num from "1" to "9":
                If is_valid(board, r, c, num):
                    board[r][c] = num
                    If solve(board): Return True
                    board[r][c] = "."  # Backtrack
            Return False # 此格填什麼都不對，向上層返回
    Return True # 沒空格了，解完
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(9^m)**
    *   m 是空格的數量。雖然理論上限很高，但數獨的規則限制會剪掉絕大部分的分支，實際運行很快。
*   **空間複雜度 (Space Complexity): O(1)**
    *   直接修改原棋盤。遞迴深度最大為 81。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self._solve(board)

    def _solve(self, board: List[List[str]]) -> bool:
        # 1. 遍歷棋盤，尋找下一個空白格位 ('.')
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    # 2. 嘗試填入數字 1 到 9
                    for num in "123456789":
                        # 3. 檢查填入該數字是否合法
                        if self._is_valid(board, r, c, num):
                            # 做選擇：填入數字
                            board[r][c] = num
                            
                            # 遞迴：嘗試填寫下一個空格
                            if self._solve(board):
                                return True
                            
                            # 回溯：如果後續解不出來，撤銷目前的選擇，恢復成空白
                            board[r][c] = '.'
                    
                    # 4. 如果 1-9 都試過且都不行，說明目前的棋盤狀態無解
                    return False
        
        # 5. 如果遍歷完整個棋盤都沒有遇到 '.'，代表數獨已解完
        return True

    def _is_valid(self, board: List[List[str]], row: int, col: int, char: str) -> bool:
        # 檢查某一格填入 char 是否符合數獨規則
        for i in range(9):
            # 檢查同一行是否已有重複
            if board[row][i] == char:
                return False
            # 檢查同一列是否已有重複
            if board[i][col] == char:
                return False
            # 檢查所在的 3x3 九宮格是否已有重複
            # (row // 3) * 3 是該九宮格左上角的行座標
            # (col // 3) * 3 是該九宮格左上角的列座標
            box_row = 3 * (row // 3) + i // 3
            box_col = 3 * (col // 3) + i % 3
            if board[box_row][box_col] == char:
                return False
        return True
```
