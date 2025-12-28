# 0046 - Permutations (全排列)

## 1. 題目理解 (Problem Comprehension)

給你一個 **不含重複數字** 的陣列 `nums` ，返回其所有可能的全排列。你可以按 **任意順序** 返回答案。

**全排列**：是指將一個集合中的所有元素以各種可能的順序重新排列。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 包含唯一數字的列表。
*   **輸出 (Output):** 所有排列的列表 (List[List[int]])。

**範例：**
輸入: `[1, 2, 3]`
輸出: `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

## 2. 思路分析 (Thought Process)

這是一個典型的「決策樹」問題。對於每個位置，我們都從剩下的數字中挑選一個填進去。

**優化思路：回溯演算法 (Backtracking)**
1.  **選擇**：從候選數字中選一個。
2.  **遞迴**：繼續處理剩下的數字。
3.  **撤銷**：當走完一條路徑後，回到上一步，改選別的數字。

**具體操作：**
*   在遞迴函式中，傳入目前的 `path`（已選數字）和 `remaining_nums`（尚未選的數字）。
*   遍歷 `remaining_nums`，每次取出一格，加入 `path`，然後進入下一層。
*   當 `remaining_nums` 為空時，說明我們完成了一種全排列。

## 3. 演算法設計 (Algorithm Design)

我們採用 **回溯法**。

**偽代碼 (Pseudo-code):**

```text
Function permute(nums):
    res = []
    
    Function backtrack(current_nums, path):
        If current_nums is empty:
            Add path to res
            Return
            
        For i from 0 to length(current_nums) - 1:
            # 選擇第 i 個數，剩下其餘的數
            next_nums = current_nums[:i] + current_nums[i+1:]
            backtrack(next_nums, path + [current_nums[i]])
            
    backtrack(nums, [])
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N * N!)**
    *   總共有 N! 個排列，每個排列需要 O(N) 的時間來拷貝和生成。
*   **空間複雜度 (Space Complexity): O(N!)**
    *   用於儲存結果。遞迴深度為 N。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # 定義回溯函式
        # current_nums: 目前還剩下哪些數字可以挑選
        # path: 目前已經挑選並排好的數字序列
        def backtrack(current_nums, path):
            # 1. 終止條件：如果沒有數字可以挑選了
            # 代表目前這條路徑已經選滿了所有數字，是一個完整的排列
            if not current_nums:
                # 將目前的路徑存入結果
                res.append(path)
                return
            
            # 2. 遍歷目前所有可以挑選的數字
            for i in range(len(current_nums)):
                # 選擇第 i 個數字
                choice = current_nums[i]
                
                # 準備傳給下一層的剩餘數字 (排除掉剛選的這一個)
                remaining = current_nums[:i] + current_nums[i+1:]
                
                # 3. 進入遞迴：
                # 將新挑選的數字接到 path 後面，並傳入縮小後的剩餘數字列表
                backtrack(remaining, path + [choice])
                
                # 註：這裡之所以不用手動「撤銷」，是因為我們在呼叫時
                # 產生了新的列表 (path + [choice])，原本層級的變數並未被修改。
                
        # 從完整的 nums 和空的 path 開始搜尋
        backtrack(nums, [])
        return res
```
