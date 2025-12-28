# 0005 - Longest Palindromic Substring (最長迴文子串)

## 1. 題目理解 (Problem Comprehension)

給定一個字串 `s`，請找出其中最長的**迴文子串 (Palindromic Substring)**。
所謂「迴文」，就是正著讀和反著讀都一樣的字串，例如 "aba" 或 "abba"。

**輸入與輸出格式：**

*   **輸入 (Input):**
    *   `s`: 一個字串。
*   **輸出 (Output):**
    *   一個字串，即 `s` 中最長的那個迴文子串。如果有多個長度一樣的，返回其中一個即可。

**範例：**
1.  `s = "babad"` -> 輸出 "bab" 或 "aba"。
2.  `s = "cbbd"` -> 輸出 "bb"。

## 2. 思路分析 (Thought Process)

### 直觀解法：暴力法

最直觀的做法是：
1.  列出所有的子串 `s[i:j]`。
2.  檢查每一個子串是否為迴文。
3.  記錄長度最長的那個。

*   **複雜度分析：**
    *   子串有 O(N^2) 個。
    *   檢查一個子串是否為迴文需要 O(N) 時間。
    *   總時間複雜度 O(N^3)。這在 N 較大時會超時。

### 優化思路：中心擴展法 (Expand Around Center)

我們可以換個角度想：與其先找子串再檢查，不如先找「中心點」，然後往兩邊擴散，直到不是迴文為止。

**迴文的中心有兩種情況：**
1.  **奇數長度**：中心是一個字符，例如 "aba" 的中心是 'b'。
2.  **偶數長度**：中心是兩個字符之間，例如 "abba" 的中心是兩個 'b' 之間。

對於長度為 N 的字串：
*   有 N 個單字符中心。
*   有 N-1 個雙字符中心（相鄰兩個字符之間）。
*   總共有 2N - 1 個中心。

**策略：**
1.  遍歷這 2N - 1 個中心。
2.  對每個中心，同時向左和向右擴展 (`left--`, `right++`)，只要 `s[left] == s[right]` 就繼續。
3.  記錄下每個中心能擴展到的最大長度，並更新全局最大值。

## 3. 演算法設計 (Algorithm Design)

我們採用 **中心擴展法**。

**偽代碼 (Pseudo-code):**

```text
Function longestPalindrome(s):
    If s is empty, return ""
    Initialize start = 0, end = 0

    For i from 0 to length(s) - 1:
        # 情況 1: 奇數長度，以 s[i] 為中心
        len1 = expandAroundCenter(s, i, i)
        
        # 情況 2: 偶數長度，以 s[i] 和 s[i+1] 為中心
        len2 = expandAroundCenter(s, i, i + 1)
        
        len = max(len1, len2)
        
        If len > end - start:
            # 更新最長迴文的起始和結束位置
            start = i - (len - 1) / 2
            end = i + len / 2

    Return s[start : end + 1]

Function expandAroundCenter(s, left, right):
    While left >= 0 AND right < length(s) AND s[left] == s[right]:
        left--
        right++
    Return right - left - 1  (因為最後一次迴圈多減了一次 left，多加了一次 right)
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N^2)**
    *   我們遍歷了 2N-1 個中心。
    *   每個中心最多向兩邊擴展 N/2 次。
    *   雖然總體還是 O(N^2)，但實際上比暴力法快很多，因為大多數中心的擴展次數很少。而且空間複雜度低，不需額外空間。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只需要幾個變數來存儲索引，不需要額外的資料結構（如動態規劃表）。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 如果字串為空，直接返回空字串
        if not s:
            return ""
        
        # 記錄最長迴文子串的起始和結束索引
        start, end = 0, 0
        
        # 遍歷每一個可能的中心點
        for i in range(len(s)):
            # 情況 1: 以 s[i] 為中心 (奇數長度迴文)
            len1 = self.expandAroundCenter(s, i, i)
            # 情況 2: 以 s[i] 和 s[i+1] 為中心 (偶數長度迴文)
            len2 = self.expandAroundCenter(s, i, i + 1)
            
            # 取兩者中較長的那個
            max_len = max(len1, len2)
            
            # 如果找到比目前記錄還長的迴文，更新 start 和 end
            # 注意這裡的索引計算要小心：
            # 如果 max_len 是奇數 (例如 3)，i 是中心。start = i - 1 = i - 2//2
            # 如果 max_len 是偶數 (例如 2)，i 是左邊那個中心。start = i - 0 = i - 1//2
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        # 返回找到的最長迴文子串
        return s[start:end+1]
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        # 當左右指針在範圍內，且字符相等時，繼續往兩邊擴展
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # 回圈結束時，left 和 right 已經是不符合條件的位置了
        # 例如如果是 "aba"，最後 left=-1, right=3
        # 長度 = right - left - 1 = 3 - (-1) - 1 = 3
        return right - left - 1
```
