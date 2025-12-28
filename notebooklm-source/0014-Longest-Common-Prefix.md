# 0014 - Longest Common Prefix (最長公共前綴)

## 1. 題目理解 (Problem Comprehension)

編寫一個函式來查找字串陣列中的最長公共前綴。
如果不存在公共前綴，返回空字串 `""`。

**輸入與輸出格式：**
*   **輸入 (Input):** `strs`: 一個字串列表 (List[str])。
*   **輸出 (Output):** 最長公共前綴 (str)。

**範例：**
1.  `["flower","flow","flight"]` -> `"fl"`
2.  `["dog","racecar","car"]` -> `""`

## 2. 思路分析 (Thought Process)

這道題有多種解法，最常見的有：

### 方法一：水平掃描 (Horizontal Scanning)
先拿前兩個字串找公共前綴 LCP，再拿 LCP 去跟第三個字串找公共前綴，以此類推。
*   `LCP(S1, S2, S3) = LCP(LCP(S1, S2), S3)`

### 方法二：垂直掃描 (Vertical Scanning) - **推薦**
我們一列一列地比較字符。
*   先看所有字串的第 0 個字符是否相同？相同就繼續。
*   再看所有字串的第 1 個字符是否相同？
*   一旦發現某個字串比較短（走到底了），或者某個字符不同，就立即停止。

**優點：** 如果最短的那個公共前綴非常短（甚至沒有），垂直掃描可以非常快地結束。

## 3. 演算法設計 (Algorithm Design)

我們採用 **垂直掃描** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function longestCommonPrefix(strs):
    If strs is empty, return ""
    
    For i from 0 to length(strs[0]) - 1:
        char = strs[0][i]
        
        For j from 1 to length(strs) - 1:
            # 檢查第 j 個字串是否已經走完，或者字符不匹配
            If i == length(strs[j]) OR strs[j][i] != char:
                # 返回目前的公共前綴
                Return strs[0] 從 0 到 i-1 的子串
                
    Return strs[0]
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(S)**
    *   S 是所有字串中字符的總數。在最壞的情況下（所有字串都一樣），我們需要比較每個字符。
*   **空間複雜度 (Space Complexity): O(1)**
    *   我們只使用了少數幾個索引變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 如果輸入列表為空，返回空字串
        if not strs:
            return ""
        
        # 採用垂直掃描：以第一個字串為基準，逐位比較
        # i 代表目前比較到第幾個字符
        for i in range(len(strs[0])):
            # 取出第一個字串的第 i 個字符
            char = strs[0][i]
            
            # 將這個字符與剩下的所有字串進行比較
            for j in range(1, len(strs)):
                # 如果目前的索引 i 已經超過了第 j 個字串的長度
                # 或者第 j 個字串在第 i 位與基準字符不匹配
                if i == len(strs[j]) or strs[j][i] != char:
                    # 說明公共前綴到此為止，返回之前匹配好的部分
                    return strs[0][:i]
                    
        # 如果整個迴圈跑完都沒有中斷，說明第一個字串本身就是所有人的公共前綴
        return strs[0]
```