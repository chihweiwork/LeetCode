# 0031 - Next Permutation (下一個排列)

## 1. 題目理解 (Problem Comprehension)

給你一個整數陣列 `nums` ，找出 `nums` 的下一個字典序更大的排列。

如果不存在下一個更大的排列（即目前的排列已經是最大的，如 `[3, 2, 1]`），則將陣列重排成最小的排列（即升序排列，如 `[1, 2, 3]`）。

**要求：**
*   必須 **原地 (In-place)** 修改。
*   只能使用額外的常數空間。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 整數列表。
*   **輸出 (Output):** 無（直接修改 `nums`）。

**範例：**
`[1, 2, 3]` -> `[1, 3, 2]`
`[3, 2, 1]` -> `[1, 2, 3]`
`[1, 1, 5]` -> `[1, 5, 1]`

## 2. 思路分析 (Thought Process)

我們需要找到一個比當前排列「大一點點」的排列。

**演算法步驟：**
1.  **從右往左找第一個「下降點」**：
    *   找到第一個滿足 `nums[i] < nums[i+1]` 的索引 `i`。
    *   如果找不到（即整個陣列是降序的），說明這是最大排列，直接跳到第 4 步翻轉整個陣列。
2.  **從右往左找第一個「剛好大於 `nums[i]` 的數」**：
    *   在 `i` 的右側（這部分目前是降序的），找到第一個滿足 `nums[j] > nums[i]` 的索引 `j`。
3.  **交換 `nums[i]` 和 `nums[j]`**：
    *   這樣我們在 `i` 位置放了一個稍大一點的數。
4.  **反轉 `i` 之後的部分**：
    *   因為 `i` 之後的部分原本是降序的，反轉後會變成升序，這能保證我們得到的排列是所有「大於原排列」中最小的那一個（即「下一個」）。

## 3. 演算法設計 (Algorithm Design)

我們採用 **標準下一個排列演算法**。

**偽代碼 (Pseudo-code):**

```text
Function nextPermutation(nums):
    n = length(nums)
    i = n - 2
    
    # 1. 找下降點
    While i >= 0 and nums[i] >= nums[i+1]:
        i = i - 1
        
    If i >= 0:
        # 2. 找剛好大的數
        j = n - 1
        While j >= 0 and nums[j] <= nums[i]:
            j = j - 1
        # 3. 交換
        Swap(nums, i, j)
        
    # 4. 反轉後面的部分
    Reverse(nums, i + 1, n - 1)
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   我們最多遍歷兩次陣列，並進行一次反轉操作。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # 1. 從右往左尋找第一個「升序對」 (nums[i] < nums[i+1])
        # 這意味著 i 之後的部分都是降序的
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        # 如果找到了這樣的 i (即 i >= 0)
        if i >= 0:
            # 2. 在右側的降序序列中，從右往左找到第一個比 nums[i] 大的數
            # 這個數是所有比 nums[i] 大的數中最小的一個
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            
            # 3. 交換這兩個數
            # 現在 i 位置變大了一點點
            nums[i], nums[j] = nums[j], nums[i]
            
        # 4. 關鍵一步：將 i 之後的部分反轉
        # 既然 i 之後原本是降序的，反轉後就會變成最小的升序排列
        # 這樣才能確保我們得到的是「下一個」緊鄰的較大排列
        self.reverse(nums, i + 1, n - 1)
        
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        # 輔助函式：原地反轉陣列的部分區間
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
```
