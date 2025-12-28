# 0016 - 3Sum Closest (最接近的三數之和)

## 1. 題目理解 (Problem Comprehension)

給你一個包含 `n` 個整數的陣列 `nums` 和一個目標值 `target`。請從 `nums` 中找出三個整數，使得它們的和與 `target` 最接近。

返回這三個整數的和。

**輸入與輸出格式：**
*   **輸入 (Input):**
    *   `nums`: 整數列表。
    *   `target`: 目標值。
*   **輸出 (Output):** 最接近 `target` 的三數之和。

**假設：**
*   每組輸入都恰好只有一個解。

**範例：**
`nums = [-1, 2, 1, -4], target = 1`
輸出: `2` (因為 `-1 + 2 + 1 = 2`，最接近 1)

## 2. 思路分析 (Thought Process)

這道題是 `0015 - 3Sum` 的變體。在 3Sum 中我們是在找等於 0 的組合，而這裡我們是在找「距離最小」的組合。

**優化思路：排序 + 雙指針**
同樣地，我們可以利用排序來簡化問題：
1.  **排序**：將陣列由小到大排序。
2.  **固定一個數**：遍歷陣列中的 `nums[i]`。
3.  **雙指針尋找**：在剩下的區間中使用 `left` 和 `right` 指針。
4.  **更新最接近值**：
    *   計算 `current_sum = nums[i] + nums[left] + nums[right]`。
    *   如果 `abs(current_sum - target)` 比目前記錄的最小差距還小，則更新結果。
    *   根據 `current_sum` 與 `target` 的大小關係來移動指針：
        *   `current_sum < target`：我們需要更大的和，所以 `left++`。
        *   `current_sum > target`：我們需要更小的和，所以 `right--`。
        *   `current_sum == target`：直接返回結果，因為差距為 0 是最完美的。

## 3. 演算法設計 (Algorithm Design)

我們採用 **排序 + 雙指針** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function threeSumClosest(nums, target):
    Sort nums
    closest_sum = nums[0] + nums[1] + nums[2]
    
    For i from 0 to n - 3:
        left = i + 1
        right = n - 1
        While left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            If current_sum == target:
                Return current_sum
            
            If abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
                
            If current_sum < target:
                left++
            Else:
                right--
                
    Return closest_sum
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N^2)**
    *   排序需要 O(N log N)。
    *   外部迴圈跑 N 次，內部雙指針跑 N 次。
*   **空間複雜度 (Space Complexity): O(1)** (或排序所需的 O(N))。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 1. 排序是雙指針法的基礎
        nums.sort()
        n = len(nums)
        # 初始化為前三個數的和
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # 2. 遍歷並固定第一個數
        for i in range(n - 2):
            # 優化：跳過重複的數
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 3. 使用雙指針在剩餘範圍尋找
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # 如果剛好等於 target，直接返回
                if current_sum == target:
                    return current_sum
                
                # 更新最接近的累計和
                # 如果當前和與目標的差距，小於之前記錄的差距
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # 4. 根據大小關係移動指針
                if current_sum < target:
                    # 當前和小了，左指針往右移來增加總和
                    left += 1
                else:
                    # 當前和大了，右指針往左移來減小總和
                    right -= 1
                    
        return closest_sum
```
