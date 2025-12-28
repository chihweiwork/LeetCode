# 0039 - Combination Sum (組合總和)

## 1. 題目理解 (Problem Comprehension)

給你一個 **無重複元素** 的整數陣列 `candidates` 和一個目標整數 `target` ，找出 `candidates` 中可以使數字和為目標數 `target` 的所有 **不重複組合** 。

**關鍵規則：**
1.  `candidates` 中的數字可以 **無限制重複選擇**。
2.  組合中的數字順序不重要，只要數字出現的次數相同就被視為同一個組合。
3.  `target` 是一個正整數。

**輸入與輸出格式：**
*   **輸入 (Input):** `candidates`: 整數列表, `target`: 目標和。
*   **輸出 (Output):** 包含所有符合條件的子列表的列表。

**範例：**
輸入: `candidates = [2,3,6,7], target = 7`
輸出: `[[2,2,3],[7]]`

## 2. 思路分析 (Thought Process)

這是一個典型的搜尋空間問題，我們需要探索所有可能的數字組合。因為數字可以重複使用，且我們需要列出所有具體的組合，**回溯演算法 (Backtracking)** 是最合適的選擇。

**如何構建決策樹？**
在每一個步驟，我們都可以從 `candidates` 中選擇一個數字：
*   **選擇後**：`target` 減少。
*   **因為可以重複使用**：下一步我們依然可以從當前的數字開始選。
*   **為了避免重複組合**：我們只往後選，不回頭選之前的數字。

**優化：剪枝 (Pruning)**
如果我們對 `candidates` 進行**排序**，那麼當我們發現某個數字已經大於剩餘的 `target` 時，後面的數字肯定也大於 `target`，我們可以立即停止當前分支的搜尋。

## 3. 演算法設計 (Algorithm Design)

我們採用 **回溯法 + 剪枝**。

**偽代碼 (Pseudo-code):**

```text
Function combinationSum(candidates, target):
    Sort candidates
    res = []
    
    Function backtrack(remain, path, start_index):
        If remain == 0:
            Add path to res
            Return
            
        For i from start_index to length(candidates) - 1:
            # 剪枝
            If candidates[i] > remain: Break
            
            # 選擇
            path.push(candidates[i])
            # 遞迴，注意這裡還是傳 i，因為可以重複選
            backtrack(remain - candidates[i], path, i)
            # 撤銷
            path.pop()
            
    backtrack(target, [], 0)
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N^(T/M))**
    *   N 是候選數字量，T 是目標值，M 是候選中的最小數值。這是鬆散的上界，實際因為剪枝會快很多。
*   **空間複雜度 (Space Complexity): O(T/M)**
    *   主要是遞迴堆疊的深度。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 1. 先對陣列進行排序，這對於後面的「剪枝」優化至關重要
        candidates.sort()
        
        # 2. 定義回溯函式
        # remain: 還剩多少數額要湊齊
        # path: 目前已經選擇的數字組合
        # start_index: 從哪個位置開始選擇，避免回頭選導致重複組合
        def backtrack(remain, path, start_index):
            # 基礎情況：剛好湊齊
            if remain == 0:
                # 存入結果（記得要做一份複本，因為 path 在回溯中會變動）
                res.append(list(path))
                return
            
            # 3. 遍歷候選數字
            for i in range(start_index, len(candidates)):
                # [剪枝優化]
                # 因為 candidates 已經排序過，如果目前的數字已經大於餘額，
                # 後面更大的數字也絕對不可能湊齊，直接跳出迴圈
                if candidates[i] > remain:
                    break
                
                # 4. 做選擇：將數字加入目前的組合
                path.append(candidates[i])
                
                # 5. 遞迴搜尋：
                # 注意第二個參數依然傳入 i，而不是 i + 1
                # 因為題目允許「無限重複選擇」同一個數字
                backtrack(remain - candidates[i], path, i)
                
                # 6. 回溯：撤銷剛才的選擇，嘗試下一個數字
                path.pop()
                
        # 從第 0 個位置開始搜尋目標金額
        backtrack(target, [], 0)
        return res
```
