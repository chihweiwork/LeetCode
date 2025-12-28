# 0032 - Longest Valid Parentheses (最長有效括號)

## 1. 題目理解 (Problem Comprehension)

給你一個只包含 `'('` 和 `')'` 的字串，找出最長的包含有效括號的子串的長度。

這是一道 LeetCode 的 **Hard** 題目。

**輸入與輸出格式：**
*   **輸入 (Input):** `s`: 只包含 `(` 和 `)` 的字串。
*   **輸出 (Output):** 最長有效子串的長度 (int)。

**範例：**
1.  `"(()"` -> `2` (有效子串是 "()")
2.  `")()())"` -> `4` (有效子串是 "()()")
3.  `""` -> `0`

## 2. 思路分析 (Thought Process)

這題可以用動態規劃 (DP) 或堆疊 (Stack) 來解決。我們這裡介紹更直觀的堆疊做法。

**優化思路：堆疊 (Stack) 記錄索引**
在一般的「判斷合法括號」問題中，我們只在堆疊裡放括號。但在這題中，我們要在堆疊裡放**索引 (Index)**，這樣我們才能計算長度。

**關鍵技巧：**
*   **初始化**：我們在堆疊中預先放入 `-1`。這是一個「參照點」，用來計算從字串開頭開始的有效長度。
*   **遇到 `(`**：將目前的索引 `i` 推入堆疊。
*   **遇到 `)`**：
    1.  彈出堆疊頂部元素。
    2.  如果堆疊變**空**了：說明這個 `)` 沒有匹配的左括號。我們將目前的索引 `i` 推入堆疊，作為新的「參照點」。
    3.  如果堆疊**不為空**：說明匹配成功了！目前的有效長度就是 `當前索引 i - 堆疊頂部元素`。更新最大長度。

## 3. 演算法設計 (Algorithm Design)

我們採用 **堆疊 (Stack)** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function longestValidParentheses(s):
    Initialize stack = [-1]
    Initialize max_len = 0
    
    For i, char in s:
        If char == '(':
            stack.push(i)
        Else:
            stack.pop()
            If stack is empty:
                # 無法配對，更新參照點
                stack.push(i)
            Else:
                # 配對成功，計算長度
                current_len = i - stack.top()
                max_len = max(max_len, current_len)
                
    Return max_len
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   只需要遍歷一次字串。
*   **空間複雜度 (Space Complexity): O(N)**
    *   在最壞情況下（全是左括號），堆疊的大小會達到 N。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 1. 建立一個堆疊，用來儲存括號的索引 (Index)
        # 初始化為 -1，這是一個「虛擬的最後一個不合法右括號的位置」
        # 它能幫助我們計算從字串開頭開始的有效長度
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # 2. 遇到左括號，將它的位置存入堆疊
                stack.append(i)
            else:
                # 3. 遇到右括號，先彈出最近的一個左括號索引
                stack.pop()
                
                if not stack:
                    # 如果彈出後堆疊變空了，說明這個右括號沒有匹配的左括號
                    # 我們將它作為新的「最後一個不合法位置」存入堆疊
                    stack.append(i)
                else:
                    # 如果堆疊不為空，說明配對成功了！
                    # 目前最長有效括號的長度 = 目前索引 - 堆疊頂部剩餘的索引
                    # 堆疊頂部的索引是「上一個沒被匹配的位置」
                    current_len = i - stack[-1]
                    if current_len > max_len:
                        max_len = current_len
                        
        return max_len
```
