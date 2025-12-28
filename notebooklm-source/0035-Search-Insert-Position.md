# 0035 - Search Insert Position (搜索插入位置)

## 1. 題目理解 (Problem Comprehension)

給定一個排序陣列和一個目標值，在陣列中找到目標值，並返回其索引。如果目標值不存在於陣列中，返回它將會被按順序插入的位置。

**關鍵要求：**
*   陣列是排序好的。
*   陣列中沒有重複數字。
*   演算法的時間複雜度必須是 **O(log n)**。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 有序整數列表, `target`: 目標值。
*   **輸出 (Output):** 索引 (int)。

**範例：**
輸入: `[1, 3, 5, 6], 5` -> 輸出: `2`
輸入: `[1, 3, 5, 6], 2` -> 輸出: `1`

## 2. 思路分析 (Thought Process)

這是一道非常經典的二分搜尋法應用題。

**優化思路：二分搜尋 (Binary Search)**
我們可以使用標準的二分搜尋。當搜尋結束且沒有找到 `target` 時，**`left` 指針所在的位置，恰好就是該數字應該被插入的位置**。

**為什麼？**
當迴圈結束時，`left > right`。此時：
*   所有小於 `target` 的數都在 `left` 的左邊。
*   所有大於 `target` 的數都在 `left`（包含自己）的右邊。
所以 `left` 就是插入點。

## 3. 演算法設計 (Algorithm Design)

我們採用 **標準二分搜尋法**。

**偽代碼 (Pseudo-code):**

```text
Function searchInsert(nums, target):
    left = 0
    right = length(nums) - 1
    
    While left <= right:
        mid = (left + right) / 2
        If nums[mid] == target:
            Return mid
        Else if nums[mid] < target:
            left = mid + 1
        Else:
            right = mid - 1
            
    # 如果沒找到，left 就是插入位置
    Return left
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(log N)**
    *   標準二分搜尋。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 使用左右雙指針來進行二分搜尋
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # 取得中間索引
            mid = (left + right) // 2
            
            # 如果剛好等於目標值，直接返回索引
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # 如果中間值比目標小，代表目標在右半邊
                left = mid + 1
            else:
                # 如果中間值比目標大，代表目標在左半邊
                right = mid - 1
                
        # 關鍵點：當迴圈結束且未找到 target 時
        # left 指針會停在第一個「大於目標值」的元素位置上
        # 這正好就是 target 應該被插入的位置
        return left
```
