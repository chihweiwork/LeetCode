# 0044 - Wildcard Matching (萬用字元匹配)

## 1. 題目理解 (Problem Comprehension)

給你一個輸入字串 `s` 和一個模式 `p` ，請你實現一個支持 `'?'` 和 `'*'` 的萬用字元匹配：

*   `'?'`：可以匹配任何**單個**字符。
*   `'*'`：可以匹配**任意序列**的字符（包括空序列）。
*   匹配必須覆蓋**整個**輸入字串。

這是一道 LeetCode 的 **Hard** 題目。

**輸入與輸出格式：**
*   **輸入 (Input):** `s`, `p`: 字串。
*   **輸出 (Output):** `True` 或 `False`。

**範例：**
1.  `s = "aa", p = "*"` -> `True`
2.  `s = "cb", p = "?a"` -> `False`
3.  `s = "adceb", p = "*a*b"` -> `True`

## 2. 思路分析 (Thought Process)

這道題跟 `0010 - Regular Expression Matching` 很像，但規則略有不同。這裡的 `*` 是獨立的萬用字元，可以代表任何長度的字串。

**優化思路：動態規劃 (Dynamic Programming)**
我們定義 `dp[i][j]` 表示 `s` 的前 `i` 個字符與 `p` 的前 `j` 個字符是否匹配。

**轉移方程：**
1.  **如果 `p[j-1] == '*'`**：
    *   **情況 A：`*` 匹配空字串**。那麼 `dp[i][j] = dp[i][j-1]` (無視這個 `*`)。
    *   **情況 B：`*` 匹配一個或多個字符**。那麼 `dp[i][j] = dp[i-1][j]` (保留這個 `*` 繼續匹配 `s` 的前一個位置)。
    *   結論：`dp[i][j] = dp[i][j-1] or dp[i-1][j]`。
2.  **如果 `p[j-1] == '?'` 或 `p[j-1] == s[i-1]`**：
    *   目前的字符匹配成功，取決於之前的結果。
    *   結論：`dp[i][j] = dp[i-1][j-1]`。
3.  **否則**：
    *   不匹配，`dp[i][j] = False`。

**基礎情況 (Base Case)：**
*   `dp[0][0] = True` (空字串與空模式匹配)。
*   `dp[0][j]`：如果模式前 `j` 個全是 `*`，則為 `True`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **二維動態規劃**。

**偽代碼 (Pseudo-code):**

```text
Function isMatch(s, p):
    m = length(s), n = length(p)
    dp = array [m+1][n+1] initialized to False
    dp[0][0] = True
    
    # 處理開頭的 *
    For j from 1 to n:
        If p[j-1] == '*': dp[0][j] = dp[0][j-1]
        Else: break
        
    For i from 1 to m:
        For j from 1 to n:
            If p[j-1] == '*':
                dp[i][j] = dp[i][j-1] OR dp[i-1][j]
            Else if p[j-1] == '?' OR p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
                
    Return dp[m][n]
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(M * N)**
    *   填滿一個 M*N 的表格。
*   **空間複雜度 (Space Complexity): O(M * N)**
    *   使用二維陣列（可優化至 O(N)）。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # 1. 建立 DP 表格，長度各加 1 用來代表「空字串」的情況
        # dp[i][j] 代表 s 的前 i 個字符與 p 的前 j 個字符是否匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # 2. 基礎情況：空對空是匹配的
        dp[0][0] = True
        
        # 3. 初始化第一行 (s 是空，p 有內容)
        # 只有當 p 全部由 '*' 組成時，才能匹配空字串 s
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
            else:
                # 只要遇到一個不是 '*' 的，後面就都不可能匹配空字串了
                break
                
        # 4. 開始填充表格
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 情況一：模式目前的字符是 '*'
                if p[j - 1] == '*':
                    # '*' 有兩種可能：
                    # dp[i][j-1]: '*' 匹配 0 個字符 (當作它不存在)
                    # dp[i-1][j]: '*' 匹配 1 個或多個字符 (消耗 s 的一個字符後，依然保留 p 的 '*')
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                
                # 情況二：模式目前的字符是 '?' 或者與 s 的字符剛好相等
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # 匹配成功，結果取決於「左上角」 (即 s 和 p 各少一個字符時的結果)
                    dp[i][j] = dp[i - 1][j - 1]
                    
                # 情況三：不匹配 (預設值就是 False，所以可以不寫)
                    
        return dp[m][n]
```
