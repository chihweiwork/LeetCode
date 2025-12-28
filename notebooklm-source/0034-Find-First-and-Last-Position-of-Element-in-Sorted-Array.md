# 0034 - Find First and Last Position of Element in Sorted Array (在排序陣列中查找元素的第一個和最後一個位置)

## 1. 題目理解 (Problem Comprehension)

給你一個按照非遞減順序排列的整數陣列 `nums`，以及一個目標值 `target`。請你找出給定目標值在陣列中的開始位置和結束位置。

如果陣列中不存在目標值 `target`，返回 `[-1, -1]`。

**要求：**
*   演算法的時間複雜度必須是 **O(log n)**。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 有序整數列表, `target`: 目標值。
*   **輸出 (Output):** 包含兩個整數的列表，代表起始與結束位置。

**範例：**
輸入: `nums = [5,7,7,8,8,10], target = 8`
輸出: `[3, 4]`

## 2. 思路分析 (Thought Process)

由於要求 O(log N) 的時間複雜度，我們直覺地想到二分搜尋法。普通的二分搜尋法只能幫我們找到「其中一個」目標值，但目標值可能有重複，分佈在一個區間內。

**優化思路：兩次二分搜尋**
我們可以分別尋找目標值的**左邊界**和**右邊界**。

1.  **尋找左邊界**：
    *   在標準二分搜尋中，當 `nums[mid] == target` 時，我們不立即停止，而是記錄下這個位置，並繼續往**左半邊**搜尋 (`right = mid - 1`)，看看還有沒有更靠左的 `target`。
2.  **尋找右邊界**：
    *   當 `nums[mid] == target` 時，我們記錄下這個位置，並繼續往**右半邊**搜尋 (`left = mid + 1`)，看看還有沒有更靠右的 `target`。

這樣通過兩次搜尋，我們就能準確鎖定 `target` 的範圍。

## 3. 演算法設計 (Algorithm Design)

我們採用 **改進的二分搜尋法**。

**偽代碼 (Pseudo-code):**

```text
Function searchRange(nums, target):
    start = findBound(nums, target, is_left=True)
    end = findBound(nums, target, is_left=False)
    Return [start, end]

Function findBound(nums, target, is_left):
    left = 0, right = length(nums) - 1
    bound = -1
    While left <= right:
        mid = (left + right) / 2
        If nums[mid] == target:
            bound = mid
            If is_left: right = mid - 1
            Else: left = mid + 1
        Else if nums[mid] > target:
            right = mid - 1
        Else:
            left = mid + 1
    Return bound
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(log N)**
    *   兩次獨立的二分搜尋，總共是 2 * log N。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 輔助函式：用二分搜尋法尋找邊界
        # is_left 為 True 時尋找最左邊的匹配位置，False 時尋找最右邊
        def findBound(is_left: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    # 找到了目標值，先記錄下目前的索引
                    bound = mid
                    # 關鍵：為了找到邊界，我們不停止搜尋
                    if is_left:
                        # 尋找左邊界，所以繼續往左半邊縮小範圍
                        right = mid - 1
                    else:
                        # 尋找右邊界，所以繼續往右半邊縮小範圍
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return bound
            
        # 分別呼叫兩次二分搜尋
        start = findBound(is_left=True)
        end = findBound(is_left=False)
        
        return [start, end]
```
