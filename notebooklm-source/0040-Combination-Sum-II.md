# 0040 - Combination Sum II (組合總和 II)

## 1. 題目理解 (Problem Comprehension)

給你一個整數陣列 `candidates` 和一個目標數 `target` ，找出 `candidates` 中所有可以使數字和為 `target` 的組合。

**關鍵規則與變更：**
1.  `candidates` 中的每個數字在每個組合中 **只能使用一次** 。
2.  `candidates` 中可能包含 **重複的數字**（例如有兩個 `1`）。
3.  解集不能包含重複的組合。

這道題是 `0039 - Combination Sum` 的變體，差別在於處理重複元素的方式。

**輸入與輸出格式：**
*   **輸入 (Input):** `candidates`: 包含（可能有重複）數字的列表, `target`: 目標和。
*   **輸出 (Output):** 所有不重複的組合列表。

## 2. 思路分析 (Thought Process)

這題有兩個主要挑戰：
1.  **每個數字只能用一次**：這很簡單，在遞迴時將索引加 1 (`i + 1`) 即可。
2.  **避免結果中出現重複組合**：這是重點。如果 `candidates = [1, 1, 7]`，選第一個 `1` 和 `7` 得到 `[1, 7]`，選第二個 `1` 和 `7` 也會得到 `[1, 7]`。這就是重複。

**優化思路：排序 + 層級去重**
1.  **排序**：同樣先將 `candidates` 排序。
2.  **層級去重**：在遍歷當前層級的候選數字時，如果發現當前的數字跟前一個一樣（且前一個沒被選中），則跳過。
    *   這代表我們已經嘗試過以這個數值作為該位置的組合了。

## 3. 演算法設計 (Algorithm Design)

我們採用 **回溯法 + 同層去重**。

**偽代碼 (Pseudo-code):**

```text
Function combinationSum2(candidates, target):
    Sort candidates
    res = []
    
    Function backtrack(remain, path, start_index):
        If remain == 0:
            Add path to res
            Return
            
        For i from start_index to length(candidates) - 1:
            # 剪枝
            If candidates[i] > remain: Break
            
            # 同層去重：如果目前數字跟上一個一樣，跳過
            If i > start_index AND candidates[i] == candidates[i-1]:
                Continue
            
            # 選擇並遞迴（傳入 i + 1，表示不可重複選）
            path.push(candidates[i])
            backtrack(remain - candidates[i], path, i + 1)
            path.pop()
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(2^N * N)**
    *   在最壞情況下，每個數字都有選或不選兩種可能。
*   **空間複雜度 (Space Complexity): O(N)**
    *   遞迴深度最大為 N。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. 排序是處理重複元素的核心
        candidates.sort()
        res = []
        
        def backtrack(remain, path, start_index):
            # 基礎情況：湊齊目標值
            if remain == 0:
                res.append(list(path))
                return
            
            for i in range(start_index, len(candidates)):
                # [優化：剪枝] 
                # 剩下的數一定比 candidates[i] 大，所以不可能湊齊
                if candidates[i] > remain:
                    break
                
                # [關鍵：去重]
                # 如果當前數字與前一個數字相同，且前一個數字是在「同一層」被跳過的
                # 我們就不再重複嘗試這個數字，否則會產生重複的組合路徑
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                # 做選擇
                path.append(candidates[i])
                
                # 遞迴：傳入 i + 1
                # 因為同一個索引的數字不能重複使用
                backtrack(remain - candidates[i], path, i + 1)
                
                # 回溯
                path.pop()
                
        backtrack(target, [], 0)
        return res
```
