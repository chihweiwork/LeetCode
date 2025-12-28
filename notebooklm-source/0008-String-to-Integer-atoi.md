# 0008 - String to Integer (atoi) (字串轉換整數)

## 1. 題目理解 (Problem Comprehension)

這道題目要求我們實現一個類似 C 語言中的 `atoi` 函式，將一個字串轉換成一個 32 位元的有號整數。

**轉換規則：**
1.  **忽略前導空格**：跳過字串開頭的所有空白字符。
2.  **判斷符號**：檢查第一個非空格字符是否為 `'+'` 或 `'-'`，這決定了最終結果的正負。如果都沒有，預設為正。
3.  **讀取數字**：讀取接下來的所有數字字符，直到遇到第一個非數字字符或字串結束。忽略後面的所有內容。
4.  **範圍限制**：如果轉換後的數字超出了 32 位元有號整數的範圍 `[-2^31, 2^31 - 1]`，則將其限制（Clamp）在邊界值。
5.  **無效情況**：如果第一個非空格字符不是符號或數字，或者字串只有空格，則返回 0。

## 2. 思路分析 (Thought Process)

這是一道典型的「字串處理」與「邊界處理」題目。我們需要按照題目要求的順序，一步一步進行檢查。

**步驟分解：**
1.  **清理空白**：使用 `strip()` 或手動移動索引跳過空格。
2.  **處理正負號**：檢查第一個字符，如果是 `'+'` 或 `'-'`，記錄符號並將索引往後移。
3.  **逐位轉換數字**：
    *   遍歷剩下的字符。
    *   如果是數字，將其轉換為整數並累加：`res = res * 10 + int(char)`。
    *   如果不是數字，立即停止。
4.  **處理邊界 (Clamp)**：
    *   Python 的整數不會溢位，所以我們可以先算出完整結果，最後再檢查是否超出 `[-2^31, 2^31 - 1]`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **線性遍歷與規則檢查**。

**偽代碼 (Pseudo-code):**

```text
Function myAtoi(s):
    1. s = trim whitespace from start of s
    2. If s is empty, return 0
    
    3. Initialize sign = 1, index = 0
    4. If s[0] == '+':
           index++
       Else if s[0] == '-':
           sign = -1
           index++
    
    5. Initialize res = 0
    6. While index < length(s) and s[index] is a digit:
           res = res * 10 + digit(s[index])
           index++
    
    7. res = res * sign
    
    8. Clamp res to [-2^31, 2^31 - 1]
    
    9. Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   我們最多只需要遍歷字串一次。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只需要幾個變數來存儲結果、符號和索引。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. 移除字串開頭和結尾的空白字符
        s = s.strip()
        
        # 2. 如果清理後字串為空，直接返回 0
        if not s:
            return 0
        
        sign = 1  # 預設符號為正
        i = 0     # 當前處理字串的索引
        
        # 3. 處理符號部分
        if s[i] == '+':
            # 遇到正號，索引往後移，符號不變
            i += 1
        elif s[i] == '-':
            # 遇到負號，索引往後移，符號設為 -1
            sign = -1
            i += 1
            
        res = 0
        # 4. 遍歷字串，直到遇到非數字字符或結束
        while i < len(s) and s[i].isdigit():
            # 將目前的數字加到結果中
            # int(s[i]) 將字符 '5' 轉為整數 5
            res = res * 10 + int(s[i])
            i += 1
            
        # 5. 加上符號
        res *= sign
        
        # 6. 處理 32 位元溢位限制 (Clamping)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res
```
