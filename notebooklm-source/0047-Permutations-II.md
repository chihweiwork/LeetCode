# 0047 - Permutations II (全排列 II)

## 1. 題目理解 (Problem Comprehension)

給你一個可包含 **重複數字** 的序列 `nums` ，按 **任意順序** 返回所有不重複的全排列。

這道題是 `0046 - Permutations` 的變體，增加了「去重」的挑戰。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 可能包含重複數字的列表。
*   **輸出 (Output):** 所有不重複排列的列表。

**範例：**
輸入: `[1, 1, 2]`
輸出: `[[1,1,2], [1,2,1], [2,1,1]]`

## 2. 思路分析 (Thought Process)

如果在 `[1, 1, 2]` 中，我們像之前一樣處理，我們會把第一個 `1` 作為開頭生成排列，然後又把第二個 `1` 作為開頭生成同樣的排列。

**優化思路：排序 + 層級去重**
要避免生成重複的排列，最有效的方法是：
1.  **排序**：先將 `nums` 由小到大排序，讓相同的數字排在一起。
2.  **層級去重**：在每一層遞迴中，如果當前的數字與前一個數字相同（`nums[i] == nums[i-1]`），則直接跳過。
    *   這代表我們在「這個位置」上已經嘗試過這個數值了，不需要再次嘗試。

## 3. 演算法設計 (Algorithm Design)

我們採用 **回溯法 + 同層去重**。

**偽代碼 (Pseudo-code):**

```text
Function permuteUnique(nums):
    Sort nums
    res = []
    
    Function backtrack(current_nums, path):
        If current_nums is empty:
            Add path to res
            Return
            
        For i from 0 to length(current_nums) - 1:
            # 去重：如果跟前一個數字一樣，跳過
            If i > 0 AND current_nums[i] == current_nums[i-1]:
                Continue
            
            remaining = current_nums[:i] + current_nums[i+1:]
            backtrack(remaining, path + [current_nums[i]])
            
    backtrack(nums, [])
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N * N!)**
    *   排列的數量級別。
*   **空間複雜度 (Space Complexity): O(N!)**
    *   結果集的大小。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 1. 排序是去重的關鍵
        # 排序後相同的數字會相鄰，我們就可以輕易判斷是否重複
        nums.sort()
        res = []
        
        # 定義回溯函式
        # current_nums: 當前層級還剩下哪些數字可以選
        # path: 目前已經選好的排列部分
        def backtrack(current_nums, path):
            # 2. 終止條件：數字選完了
            if not current_nums:
                res.append(path)
                return
            
            # 3. 遍歷候選數字
            for i in range(len(current_nums)):
                # [關鍵：去重邏輯]
                # 如果目前的數字跟前一個數字相同
                # 因為我們是從左往右選，如果前一個相同的數字剛被「選過」並回溯回來，
                # 我們就不應該在「同一個位置」再次選擇相同的數字。
                if i > 0 and current_nums[i] == current_nums[i - 1]:
                    continue
                
                # 4. 遞迴搜尋
                # 傳入排除掉目前選擇後的剩餘列表
                backtrack(current_nums[:i] + current_nums[i+1:], path + [current_nums[i]])
                
        # 從完整的 nums 開始搜尋
        backtrack(nums, [])
        return res
```
