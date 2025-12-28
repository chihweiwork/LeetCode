# 0017 - Letter Combinations of a Phone Number (電話號碼的字母組合)

## 1. 題目理解 (Problem Comprehension)

給定一個僅包含數字 `2-9` 的字串，返回所有它能表示的字母組合。答案可以按 **任意順序** 返回。

給出數字到字母的映射（與電話按鍵相同）：
*   2: abc, 3: def, 4: ghi, 5: jkl, 6: mno, 7: pqrs, 8: tuv, 9: wxyz

**輸入與輸出格式：**
*   **輸入 (Input):** `digits`: 一個由數字組成的字串。
*   **輸出 (Output):** 字串列表，包含所有可能的組合。

**範例：**
`digits = "23"`
輸出: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

## 2. 思路分析 (Thought Process)

這是一個典型的組合問題。我們需要從第一個數字對應的字母中選一個，再從第二個數字選一個...以此類推。

當我們需要窮舉所有可能的「路徑」或「組合」時，**回溯演算法 (Backtracking)** 是最合適的工具。

**回溯法的核心思想：**
1.  **選擇**：從當前數字對應的字母集中選一個字母。
2.  **遞迴**：移動到下一個數字，繼續選擇。
3.  **撤銷（回溯）**：當完成一條路徑後，回到上一步，改選另一個字母。

## 3. 演算法設計 (Algorithm Design)

我們採用 **深度優先搜尋 (DFS) / 回溯法**。

**偽代碼 (Pseudo-code):**

```text
Function letterCombinations(digits):
    If digits is empty, return []
    
    Map phone = {2: "abc", 3: "def", ...}
    res = []
    
    Function backtrack(index, current_path):
        # 終止條件：如果路徑長度等於數字長度
        If length(current_path) == length(digits):
            Add current_path to res
            Return
            
        # 取得當前數字對應的所有字母
        letters = phone[digits[index]]
        For each char in letters:
            # 遞迴處理下一個數字
            backtrack(index + 1, current_path + char)
            
    backtrack(0, "")
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(3^N * 4^M)**
    *   N 是對應 3 個字母的數字個數，M 是對應 4 個字母的數字個數。
    *   總組合數就是這個複雜度。
*   **空間複雜度 (Space Complexity): O(N+M)**
    *   主要是遞迴堆疊的深度。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 如果輸入為空，直接返回空列表
        if not digits:
            return []
            
        # 建立電話按鍵的對照表
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        res = []
        
        # 定義回溯函式
        # index: 目前處理到第幾個數字
        # current_path: 目前累積的字母組合
        def backtrack(index: int, current_path: str):
            # 1. 終止條件：如果累積的組合長度等於輸入的數字長度
            if len(current_path) == len(digits):
                res.append(current_path)
                return
            
            # 2. 取得當前數字對應的候選字母
            possible_letters = phone_map[digits[index]]
            
            # 3. 遍歷候選字母
            for letter in possible_letters:
                # 進入下一層遞迴，處理下一個數字
                backtrack(index + 1, current_path + letter)
                
        # 從第 0 個數字、空組合開始搜尋
        backtrack(0, "")
        return res
```
