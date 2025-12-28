# 0042 - Trapping Rain Water (接雨水)

## 1. 題目理解 (Problem Comprehension)

給你一個非負整數陣列 `height` ，每個數代表一個寬度為 1 的柱子的高度。請計算雨天之後，這些柱子之間能接住多少雨水。

這是一道非常經典的 LeetCode **Hard** 題目。

**輸入與輸出格式：**
*   **輸入 (Input):** `height`: 整數列表。
*   **輸出 (Output):** 總接水量 (int)。

**範例：**
輸入: `[0,1,0,2,1,0,1,3,2,1,2,1]`
輸出: `6`

## 2. 思路分析 (Thought Process)

雨水是怎麼被接住的？對於每一個位置 `i`，它能接住的水取決於：
1.  它左邊最高的柱子 `left_max`。
2.  它右邊最高的柱子 `right_max`。
3.  它能接的水量 = `min(left_max, right_max) - height[i]`。

如果 `min(left_max, right_max)` 比當前高度還低，接水量就是 0。

### 直觀解法：動態規劃
預先算出每個位置對應的 `left_max` 陣列和 `right_max` 陣列。
*   時間複雜度：O(N)
*   空間複雜度：O(N) 用於存儲兩個陣列。

### 優化思路：雙指針 (Two Pointers)
我們可以用兩個指針 `left` 和 `right` 從兩端向中間移動。

**關鍵邏輯**：
如果 `height[left] < height[right]`，那麼對於 `left` 位置來說，雖然我們不知道右邊真正的 `right_max` 是多少，但我們知道它一定大於等於目前的 `height[right]`。
因此，`left` 位置能接的水只受限於 `left_max`。
只要 `left_max > height[left]`，就能接水。

同理，如果 `height[right] <= height[left]`，則 `right` 位置能接的水只受限於 `right_max`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **雙指針法**。

**偽代碼 (Pseudo-code):**

```text
Function trap(height):
    left = 0, right = length - 1
    left_max = 0, right_max = 0
    res = 0
    
    While left < right:
        If height[left] < height[right]:
            If height[left] >= left_max:
                left_max = height[left]
            Else:
                res += left_max - height[left]
            left++
        Else:
            If height[right] >= right_max:
                right_max = height[right]
            Else:
                res += right_max - height[right]
            right--
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   只需要遍歷一次陣列。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        # 初始化左右雙指針
        left, right = 0, len(height) - 1
        # 記錄左側遇到的最高柱子和右側遇到的最高柱子
        left_max, right_max = 0, 0
        res = 0
        
        while left < right:
            # 核心邏輯：木桶原理
            # 水量取決於較短的那一邊。
            # 如果左邊比右邊矮，那麼左邊能接的水只取決於左邊的最高點
            if height[left] < height[right]:
                if height[left] >= left_max:
                    # 如果當前高度更高，更新左側最高點，接不到水
                    left_max = height[left]
                else:
                    # 如果當前高度比左側最高點矮，差距就是能接的水量
                    res += left_max - height[left]
                # 移動左指針
                left += 1
            else:
                # 同理處理右邊
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                # 移動右指針
                right -= 1
                
        return res
```
