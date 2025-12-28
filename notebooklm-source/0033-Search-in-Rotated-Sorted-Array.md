# 0033 - Search in Rotated Sorted Array (搜索旋轉排序陣列)

## 1. 題目理解 (Problem Comprehension)

整數陣列 `nums` 原本是按升序排列的，但在傳遞給函式之前，它在某個未知的下標 `k` 處進行了旋轉。
例如，`[0,1,2,4,5,6,7]` 可能變成 `[4,5,6,7,0,1,2]`。

給你旋轉後的陣列 `nums` 和一個目標值 `target` ，如果 `nums` 中存在這個目標值，則返回它的下標，否則返回 `-1` 。

**要求：**
*   演算法的時間複雜度必須是 **O(log n)**。這意味著我們必須使用二分搜尋的變體。
*   陣列中的值都是唯一的。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 旋轉後的有序列表, `target`: 目標值。
*   **輸出 (Output):** 目標值的索引 (int)。

## 2. 思路分析 (Thought Process)

雖然陣列被旋轉了，但它仍然是「局部有序」的。如果我們在中間切一刀，**左右兩半中至少有一半是完全有序的**。

**如何利用這個特點？**
1.  找到中間點 `mid`。
2.  判斷哪一邊是有序的：
    *   如果 `nums[left] <= nums[mid]`，代表**左半邊是有序的**。
    *   否則，**右半邊是有序的**。
3.  在有序的那一邊檢查 `target` 是否在範圍內：
    *   如果在，縮小範圍到那一邊。
    *   如果不在，縮小範圍到另一邊。

這個邏輯可以讓我們在每次比較中排除掉一半的元素，保持 O(log N) 的效率。

## 3. 演算法設計 (Algorithm Design)

我們採用 **二分搜尋法 (Binary Search)**。

**偽代碼 (Pseudo-code):**

```text
Function search(nums, target):
    left = 0, right = length(nums) - 1
    
    While left <= right:
        mid = (left + right) / 2
        If nums[mid] == target: Return mid
        
        # 判斷哪邊是有序的
        If nums[left] <= nums[mid]:
            # 左半邊有序
            If nums[left] <= target < nums[mid]:
                # target 在左邊
                right = mid - 1
            Else:
                # target 在右邊
                left = mid + 1
        Else:
            # 右半邊有序
            If nums[mid] < target <= nums[right]:
                # target 在右邊
                left = mid + 1
            Else:
                # target 在左邊
                right = mid - 1
    Return -1
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(log N)**
    *   標準的二分搜尋。
*   **空間複雜度 (Space Complexity): O(1)**

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
            
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # 1. 找到了直接返回
            if nums[mid] == target:
                return mid
            
            # 2. 關鍵：判斷哪一半邊是「有序」的
            # 因為是旋轉過的，兩邊一定有一邊是正常的升序
            if nums[left] <= nums[mid]:
                # 情況 A：左半邊 [left...mid] 是有序的
                # 檢查 target 是否落在這個有序區間內
                if nums[left] <= target < nums[mid]:
                    # 在區間內，將搜尋範圍縮小到左半邊
                    right = mid - 1
                else:
                    # 不在區間內，去右半邊找
                    left = mid + 1
            else:
                # 情況 B：右半邊 [mid...right] 是有序的
                # 檢查 target 是否落在這個有序區間內
                if nums[mid] < target <= nums[right]:
                    # 在區間內，將搜尋範圍縮小到右半邊
                    left = mid + 1
                else:
                    # 不在區間內，去左半邊找
                    right = mid - 1
                    
        # 3. 遍歷結束仍未找到
        return -1
```
