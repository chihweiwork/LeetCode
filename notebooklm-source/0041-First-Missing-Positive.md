# 0041 - First Missing Positive (缺失的第一個正數)

## 1. 題目理解 (Problem Comprehension)

給你一個未排序的整數陣列 `nums` ，請你找出其中沒有出現過的最小正整數。

**特別要求：**
*   時間複雜度必須為 **O(n)**。
*   空間複雜度必須為 **O(1)**。

這是一道 LeetCode 的 **Hard** 題目，難點在於如何在限制空間的情況下完成 O(n) 的搜尋。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 未排序的整數列表。
*   **輸出 (Output):** 最小的缺失正整數。

**範例：**
輸入: `[1, 2, 0]` -> 輸出: `3`
輸入: `[3, 4, -1, 1]` -> 輸出: `2`
輸入: `[7, 8, 9]` -> 輸出: `1`

## 2. 思路分析 (Thought Process)

既然空間限制在 O(1)，我們不能使用额外的 Hash Set。唯一的辦法就是 **原地利用輸入陣列本身**。

**關鍵觀察：**
對於一個長度為 `N` 的陣列，缺失的第一個正整數一定在 `[1, N+1]` 之間。
*   如果陣列剛好包含 `1, 2, ..., N`，答案就是 `N+1`。
*   否則，答案一定在 `1` 到 `N` 之間。

**優化思路：原地哈希 / 桶排序 (Cyclic Sort)**
我們可以嘗試把每個數字搬到它「應該在」的位置。
*   數字 `1` 應該放在 `nums[0]`。
*   數字 `2` 應該放在 `nums[1]`。
*   數字 `x` 應該放在 `nums[x-1]`。

**步驟：**
1.  遍歷陣列，如果當前數字 `x` 在 `[1, N]` 範圍內，且它不在正確位置 `nums[x-1]` 上，我們就把它與 `nums[x-1]` 位置上的數字交換。
2.  重複交換直到當前格子的數字正確，或者超出範圍，或者目標位置已經有正確數字（處理重複）。
3.  第二次遍歷陣列，找出第一個 `nums[i] != i + 1` 的位置，答案就是 `i + 1`。
4.  如果都符合，答案就是 `N + 1`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **原地哈希 (In-place Hashing)**。

**偽代碼 (Pseudo-code):**

```text
Function firstMissingPositive(nums):
    n = length(nums)
    
    For i from 0 to n - 1:
        # 當前數字 nums[i] 應該在索引 nums[i]-1
        While 1 <= nums[i] <= n AND nums[nums[i]-1] != nums[i]:
            Swap(nums[i], nums[nums[i]-1])
            
    For i from 0 to n - 1:
        If nums[i] != i + 1:
            Return i + 1
            
    Return n + 1
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   雖然有 `while` 迴圈，但每次交換都會把至少一個數字放到正確位置，所以總交換次數不會超過 N。
*   **空間複雜度 (Space Complexity): O(1)**
    *   直接修改原陣列。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 1. 桶排序思想：嘗試將數字 x 放到索引 x-1 的位置
        for i in range(n):
            # 只要當前數字在 [1, n] 之間，且它還沒被放在正確的位置上
            # 就持續進行交換
            # nums[nums[i]-1] != nums[i] 這一條能同時處理「位置錯誤」與「重複數字」
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                # 取得該數字應該去的索引
                correct_idx = nums[i] - 1
                
                # 交換目前位置與目標位置的數字
                # 這樣 nums[correct_idx] 就變成了 correct_idx + 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # 2. 第二次遍歷：尋找第一個「德不配位」的位置
        for i in range(n):
            # 如果索引 i 的位置存的不是 i + 1，說明 i + 1 就是缺失的最小正數
            if nums[i] != i + 1:
                return i + 1
                
        # 3. 如果 1 到 n 都整齊排列，則缺失的是下一個正數
        return n + 1
```
