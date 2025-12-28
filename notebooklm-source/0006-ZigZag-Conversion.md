# 0006 - ZigZag Conversion (Z 字形變換)

## 1. 題目理解 (Problem Comprehension)

將一個給定的字串 `s` 根據指定的行數 `numRows`，以從上到下、從左到右的 Z 字形進行排列。

例如，字串為 `"PAYPALISHIRING"`，行數為 `3` 時，排列如下：
```text
P   A   H   N
A P L S I I G
Y   I   R
```
之後，我們按行讀取字符：`"PAHNAPLSIIGYIR"`。

**輸入與輸出格式：**
*   **輸入 (Input):**
    *   `s`: 一個字串。
    *   `numRows`: 一個整數，代表行數。
*   **輸出 (Output):**
    *   變換後的字串。

## 2. 思路分析 (Thought Process)

### 直觀解法：模擬排列過程

我們不需要真的去畫出一個二維矩陣（那樣會浪費很多空間）。我們只需要知道每個字符應該屬於哪一行，然後最後按順序把每一行的字符拼接起來即可。

想像一個電梯在 `numRows` 層樓之間上下移動：
1.  從第 0 行開始，往下走 (0, 1, 2, ...)。
2.  到達第 `numRows - 1` 行後，往回走 (... 2, 1, 0)。
3.  到達第 0 行後，再次往下走。

**核心邏輯：**
*   我們用一個列表 `rows` 來儲存每一行的內容，`rows[i]` 是一個字串，代表第 `i` 行目前收集到的字符。
*   我們用一個變數 `index` 追蹤目前在哪一行。
*   我們用一個變數 `step` 來控制方向：向下走時 `step = 1`，向上走時 `step = -1`。
*   當 `index` 到達 0 或 `numRows - 1` 時，我們就反轉 `step` 的正負號。

## 3. 演算法設計 (Algorithm Design)

我們採用 **模擬與方向控制** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function convert(s, numRows):
    If numRows == 1 or numRows >= length(s):
        Return s

    Initialize rows = array of empty strings, size numRows
    Initialize index = 0
    Initialize step = 1

    For each char in s:
        Append char to rows[index]
        
        If index == 0:
            step = 1
        Else if index == numRows - 1:
            step = -1
        
        index = index + step

    Return join(rows)
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   我們只需要遍歷一次字串 `s`，其中 N 是字串的長度。
*   **空間複雜度 (Space Complexity): O(N)**
    *   我們使用了 `rows` 列表來儲存字符，最終總長度還是 N。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 如果只有一行，或者行數比字串還長，不需要變換，直接返回
        if numRows == 1 or numRows >= len(s):
            return s
        
        # 建立一個列表，用來存放每一行的字符
        rows = [''] * numRows
        
        # index 代表目前在哪一行，step 代表移動的方向 (1 是向下，-1 是向上)
        index, step = 0, 1
        
        for char in s:
            # 將當前字符加入對應的行
            rows[index] += char
            
            # 如果走到了第一行，接下來要往下走 (step = 1)
            if index == 0:
                step = 1
            # 如果走到了最後一行，接下來要往上走 (step = -1)
            elif index == numRows - 1:
                step = -1
            
            # 根據方向移動到下一行
            index += step
            
        # 最後將所有行的字串拼接起來即為答案
        return ''.join(rows)
```
