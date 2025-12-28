# 0011 - Container With Most Water (盛最多水的容器)

## 1. 題目理解 (Problem Comprehension)

給定一個長度為 `n` 的整數陣列 `height`。有 `n` 條垂線，第 `i` 條線的兩個端點分別為 `(i, 0)` 和 `(i, height[i])`。

找出其中的兩條線，使得它們與 x 軸共同構成的容器可以容納最多的水。返回容器可以儲存的最大水量。

**輸入與輸出格式：**
*   **輸入 (Input):** `height`: 一個整數列表。
*   **輸出 (Output):** `max_area`: 最大水容量（整數）。

**限制：**
*   你不能傾斜容器。
*   容量 = 底 (兩個索引之差) * 高 (兩條線中較短的那條)。

## 2. 思路分析 (Thought Process)

### 直觀解法：暴力法

檢查每一對可能的垂直線組合 `(i, j)`，計算它們能盛的水量，然後取最大值。
*   迴圈 `i` 從 0 到 `n-1`，迴圈 `j` 從 `i+1` 到 `n-1`。
*   `area = (j - i) * min(height[i], height[j])`。
*   時間複雜度：O(N^2)。當 N 很大時會超時。

### 優化思路：雙指針 (Two Pointers)

我們可以用兩個指針 `left` 和 `right` 分別指向陣列的兩端。

**為什麼這樣做有效？**
容器的容量由兩個因素決定：**寬度 (Width)** 和 **高度 (Height)**。
*   當指針在兩端時，我們擁有最大的「寬度」。
*   當我們移動指針時，「寬度」一定會變小。
*   為了補償變小的寬度，我們必須尋求更大的「高度」。
*   高度是由兩邊較短的那條線決定的。因此，如果我們移動較長的那條線，高度只會變小或不變（因為短的那條沒變），寬度又變小了，面積一定變小。
*   **結論**：我們應該移動**較短**的那條線，看看能不能換到一條更長的線來增加高度。

## 3. 演算法設計 (Algorithm Design)

我們採用 **雙指針** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function maxArea(height):
    Initialize left = 0, right = length(height) - 1
    Initialize max_area = 0

    While left < right:
        # 計算當前面積
        current_width = right - left
        current_height = min(height[left], height[right])
        current_area = current_width * current_height
        
        # 更新最大面積
        max_area = max(max_area, current_area)
        
        # 移動較短的那一邊
        If height[left] < height[right]:
            left++
        Else:
            right--

    Return max_area
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   我們只遍歷了陣列一次。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 初始化左右指針分別指向陣列的首尾
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # 容器的寬度是兩個指針之間的距離
            width = right - left
            # 容器的高度取決於左右兩條線中較短的那一條 (木桶效應)
            h = min(height[left], height[right])
            
            # 計算當前面積並更新最大值
            current_area = width * h
            if current_area > max_area:
                max_area = current_area
            
            # 核心邏輯：移動較短的那一側指針
            # 因為寬度已經在變小了，只有移動短的那邊才有機會讓高度增加，進而增加面積
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
```