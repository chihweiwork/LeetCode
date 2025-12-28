# 0022 - Generate Parentheses (生成括號)

## 1. 題目理解 (Problem Comprehension)

數字 `n` 代表括號的對數，請你設計一個函式，用於能夠生成所有可能的並且 **有效的** 括號組合。

**輸入與輸出格式：**
*   **輸入 (Input):** `n`: 括號的對數 (int)。
*   **輸出 (Output):** 所有有效的括號組合列表 (List[str])。

**範例：**
輸入: `n = 3`
輸出: `["((()))","(()())","(())()","()(())","()()()"]`

## 2. 思路分析 (Thought Process)

這是一個典型的窮舉所有可能組合的問題。對於每個位置，我們都有兩個選擇：放一個左括號 `(` 或者放一個右括號 `)`。

**但是，不是所有的組合都是有效的。如何確保有效？**
1.  **左括號的數量**：最多只能放 `n` 個左括號。
2.  **右括號的數量**：在任何時候，已放置的右括號數量不能超過左括號的數量（否則就會出現像 `())` 這樣無法匹配的情況）。

**優化思路：回溯演算法 (Backtracking)**
我們可以使用遞迴來構建字串，並在每一步根據上述規則進行「剪枝」（即只走合法的路徑）。

## 3. 演算法設計 (Algorithm Design)

我們採用 **回溯法**。

**偽代碼 (Pseudo-code):**

```text
Function generateParenthesis(n):
    res = []
    
    Function backtrack(current_s, open_count, close_count):
        # 終止條件：如果字串長度達到 2*n
        If length(current_s) == 2 * n:
            Add current_s to res
            Return
            
        # 如果左括號還沒用完，可以放左括號
        If open_count < n:
            backtrack(current_s + "(", open_count + 1, close_count)
            
        # 如果右括號比左括號少，可以放右括號
        If close_count < open_count:
            backtrack(current_s + ")", open_count, close_count + 1)
            
    backtrack("", 0, 0)
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(4^n / sqrt(n))**
    *   這與卡特蘭數 (Catalan Number) 有關，代表了有效括號組合的數量。
*   **空間複雜度 (Space Complexity): O(n)**
    *   主要是遞迴堆疊的深度。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        # 定義回溯函式
        # current_s: 目前構建中的字串
        # open_count: 已經使用的左括號數量
        # close_count: 已經使用的右括號數量
        def backtrack(current_s: str, open_count: int, close_count: int):
            # 1. 終止條件：當字串長度達到 2 * n 時，表示一組完整的組合已生成
            if len(current_s) == 2 * n:
                res.append(current_s)
                return
            
            # 2. 選擇放左括號：
            # 只要左括號的使用數量還沒達到 n，就可以繼續放
            if open_count < n:
                backtrack(current_s + '(', open_count + 1, close_count)
            
            # 3. 選擇放右括號：
            # 關鍵規則：右括號的數量必須小於目前的左括號數量
            # 這樣才能保證每一個右括號都能找到對應的左括號
            if close_count < open_count:
                backtrack(current_s + ')', open_count, close_count + 1)
                
        # 從空字串、0 個左括號、0 個右括號開始遞迴
        backtrack("", 0, 0)
        return res
```
