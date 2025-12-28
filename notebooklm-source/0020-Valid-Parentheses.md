# 0020 - Valid Parentheses (有效的括號)

## 1. 題目理解 (Problem Comprehension)

給定一個只包括 `'('`, `')'`, `'{'`, `'}'`, `'['`, `']'` 的字串 `s` ，判斷字串是否有效。

**有效字串需滿足：**
1.  左括號必須用相同類型的右括號閉合。
2.  左括號必須以正確的順序閉合。
3.  每個右括號都有一個對應的相同類型的左括號。

**輸入與輸出格式：**
*   **輸入 (Input):** `s`: 字串。
*   **輸出 (Output):** `True` 或 `False` (bool)。

**範例：**
*   `"()"` -> `True`
*   `"()[]{}"` -> `True`
*   `"(]"` -> `False`
*   `"([)]"` -> `False`
*   `"{[]}"` -> `True`

## 2. 思路分析 (Thought Process)

這是一個典型的「後進先出 (LIFO)」問題。最後一個出現的左括號，必須第一個被閉合。

**優化思路：堆疊 (Stack)**
我們可以使用一個 **堆疊 (Stack)** 來追蹤尚未閉合的左括號。

**步驟：**
1.  建立一個空的堆疊。
2.  遍歷字串中的每個字符：
    *   如果是 **左括號** (`(`, `{`, `[`):
        *   將它推入 (push) 堆疊。
    *   如果是 **右括號** (`)`, `}`, `]`):
        *   檢查堆疊是否為空？如果為空，表示沒有對應的左括號，無效。
        *   彈出 (pop) 堆疊頂端的左括號。
        *   檢查這個彈出的左括號是否與當前的右括號匹配？如果不匹配，無效。
3.  遍歷結束後，檢查堆疊是否為空：
    *   如果為空，表示所有左括號都正確閉合了，有效。
    *   如果不為空，表示有孤單的左括號，無效。

## 3. 演算法設計 (Algorithm Design)

我們採用 **堆疊 (Stack)** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function isValid(s):
    Initialize stack = []
    Initialize mapping = {')': '(', '}': '{', ']': '['}
    
    For each char in s:
        If char is a closing bracket (in mapping):
            If stack is empty:
                Return False
            top_element = stack.pop()
            If top_element != mapping[char]:
                Return False
        Else:
            # It's an opening bracket
            stack.push(char)
            
    Return stack is empty
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   我們只需要遍歷一次字串。每個字符的進棧和出棧操作都是 O(1)。
*   **空間複雜度 (Space Complexity): O(N)**
    *   在最壞情況下（全是左括號），我們需要將所有字符存入堆疊。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        # 如果字串長度是奇數，一定無法配對成功
        if len(s) % 2 != 0:
            return False
            
        # 建立一個映射表，方便我們根據右括號找到對應的左括號
        # 也可以反過來存，邏輯正確即可
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # 建立堆疊，用來存放還沒被閉合的左括號
        stack = []
        
        for char in s:
            # 如果目前字符是右括號
            if char in bracket_map:
                # 彈出堆疊頂端的元素（如果堆疊為空，給一個虛擬字符 '#'）
                top_element = stack.pop() if stack else '#'
                
                # 檢查彈出的左括號是否與當前的右括號匹配
                if bracket_map[char] != top_element:
                    return False
            else:
                # 如果是左括號，將它推入堆疊
                stack.append(char)
                    
        # 最後檢查堆疊是否為空。如果為空，代表所有的括號都完美配對
        return len(stack) == 0
```
