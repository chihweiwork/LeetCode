# 0045 - Jump Game II (跳躍遊戲 II)

## 1. 題目理解 (Problem Comprehension)

給你一個非負整數陣列 `nums` ，你最初位於陣列的第一個位置。
陣列中的每個元素代表你在該位置可以跳躍的最大長度。

你的目標是使用 **最少的跳躍次數** 到達陣列的最後一個位置。
假設你總是可以用最少的跳躍次數到達。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 整數列表。
*   **輸出 (Output):** 最少跳躍次數 (int)。

**範例：**
輸入: `[2, 3, 1, 1, 4]`
輸出: `2`
（從索引 0 跳到索引 1，再從索引 1 跳到末尾）

## 2. 思路分析 (Thought Process)

這道題可以用動態規劃 (DP) 解，但時間複雜度會是 O(N^2)。
既然要求「最少步數」，且每次跳躍都有一個範圍，我們可以用 **貪心演算法 (Greedy Algorithm)** 來達到 O(N)。

**核心思想：**
每一跳都想著「下一步我最遠能跳到哪裡」。我們不需要在當前這步就決定具體跳到哪，而是觀察在**目前這一跳能覆蓋的範圍內**，哪一個點能讓我們**下一跳跳得最遠**。

**關鍵變數：**
1.  `jumps`: 跳躍次數。
2.  `current_jump_end`: 目前這一跳最遠能到達的邊界。
3.  `farthest`: 在 `current_jump_end` 範圍內，我們能跳到的下一個最遠點。

**步驟：**
1.  遍歷陣列（除了最後一個元素，因為到達最後一個元素就結束了）。
2.  更新 `farthest = max(farthest, i + nums[i])`。
3.  如果我們走到了目前這一跳的邊界 `current_jump_end`：
    *   必須再跳一次：`jumps++`。
    *   更新邊界為剛才找到的最遠點：`current_jump_end = farthest`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **貪心演算法**。

**偽代碼 (Pseudo-code):**

```text
Function jump(nums):
    If length <= 1: Return 0
    
    jumps = 0
    current_end = 0
    farthest = 0
    
    For i from 0 to length - 2:
        farthest = max(farthest, i + nums[i])
        
        If i == current_end:
            jumps++
            current_end = farthest
            If current_end >= length - 1: Break
            
    Return jumps
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
    def jump(self, nums: List[int]) -> int:
        # 1. 基礎情況：如果只有一個元素，不需要跳躍
        if len(nums) <= 1:
            return 0
            
        jumps = 0            # 跳躍次數
        current_jump_end = 0  # 目前這一跳能到達的最遠邊界
        farthest = 0         # 在目前範圍內，下一步最遠能跳到的位置
        
        # 2. 遍歷陣列，直到倒數第二個元素
        # 為什麼不包含最後一個？因為一旦 current_jump_end 覆蓋了最後一個，就完成了
        for i in range(len(nums) - 1):
            # 3. 不斷更新從目前能跳到的所有點出發，下一次最遠能到哪裡
            farthest = max(farthest, i + nums[i])
            
            # 4. 當我們走到了目前這一跳的盡頭
            if i == current_jump_end:
                # 必須增加一次跳躍次數
                jumps += 1
                # 將「新的邊界」設為剛才尋找到的最遠點
                current_jump_end = farthest
                
                # [優化] 如果新邊界已經可以到達終點，提早結束
                if current_jump_end >= len(nums) - 1:
                    break
                    
        return jumps
```
