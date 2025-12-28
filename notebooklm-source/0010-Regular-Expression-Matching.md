# 0010 - Regular Expression Matching (正則表達式匹配)

## 1. 題目理解 (Problem Comprehension)

這是一道 LeetCode 的 **Hard** 題目。你需要實現一個簡化版的正則表達式匹配：

*   `.`：匹配任意**單個**字符。
*   `*`：匹配**零個或多個**前面的那個元素。
*   匹配必須覆蓋**整個**輸入字串 `s`。

**輸入與輸出格式：**
*   **輸入 (Input):**
    *   `s`: 待匹配的字串。
    *   `p`: 正則表達式模式。
*   **輸出 (Output):** `True` 或 `False`。

**範例：**
1.  `s = "aa", p = "a"` -> `False`
2.  `s = "aa", p = "a*"` -> `True` ('*' 匹配了兩次 'a')
3.  `s = "ab", p = ".*"` -> `True` ('.' 匹配了 'a', '*' 讓它重複匹配了 'b')

## 2. 思路分析 (Thought Process)

這題最難的地方在於 `*` 的處理。當我們遇到 `x*` 時，它可以匹配 0 個 `x`、1 個 `x`、2 個 `x` 等等。這會導致很多種分支，因此非常適合用**動態規劃 (Dynamic Programming, DP)** 來解決。

### 狀態定義
我們定義 `dp[i][j]` 表示「字串 `s` 從索引 `i` 開始的子串」是否能被「模式 `p` 從索引 `j` 開始的子串」所匹配。

### 轉移方程
1.  **首字符匹配判斷**：
    `first_match = (i < len(s)) and (p[j] == s[i] or p[j] == '.')`

2.  **處理 `*` (即檢查 `p[j+1]` 是否為 `*`)**：
    *   **情況 A：匹配 0 次**。我們直接跳過 `p[j]` 和 `p[j+1]`。
        `dp[i][j] = dp[i][j+2]`
    *   **情況 B：匹配 1 次或多次**。前提是 `first_match` 為真，然後我們繼續用同一個模式去匹配 `s` 的下一個位置。
        `dp[i][j] = first_match and dp[i+1][j]`
    *   **兩者取其一**：`dp[i][j] = (情況 A) or (情況 B)`

3.  **一般情況 (沒有 `*`)**：
    *   只要 `first_match` 為真，並且剩下的部分也匹配。
        `dp[i][j] = first_match and dp[i+1][j+1]`

### 基礎情況 (Base Case)
*   當 `i` 和 `j` 都到達末尾時，`dp[len(s)][len(p)] = True`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **自底向上 (Bottom-up) 的動態規劃**。

**偽代碼 (Pseudo-code):**

```text
Function isMatch(s, p):
    Initialize dp table [len(s)+1][len(p)+1] with False
    dp[len(s)][len(p)] = True

    For i from len(s) down to 0:
        For j from len(p)-1 down to 0:
            first_match = (i < len(s) and (p[j] == s[i] or p[j] == '.'))
            
            If j + 1 < len(p) and p[j+1] == '*':
                # Case 1: 0 occurrences, Case 2: 1+ occurrences
                dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
            Else:
                # Normal match
                dp[i][j] = first_match and dp[i+1][j+1]

    Return dp[0][0]
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(S * P)**
    *   S 和 P 分別是字串和模式的長度。我們需要填滿一個 S*P 的矩陣。
*   **空間複雜度 (Space Complexity): O(S * P)**
    *   需要一個二維陣列來儲存 DP 狀態。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] 代表 s[i:] 是否與 p[j:] 匹配
        # 我們多開一列和一行來處理空字串的情況
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # 空字串與空模式當然匹配
        dp[len(s)][len(p)] = True
        
        # 從後往前填表
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                # 檢查當前第一個字符是否匹配
                # 注意 i < len(s) 是為了防止 s 已經用完但 p 還沒完的情況
                first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
                
                # 如果下一個字符是 '*'
                if j + 1 < len(p) and p[j+1] == '*':
                    # '*' 的兩種選法：
                    # 1. 匹配 0 個：忽略目前的字符和 '*'，看 p[j+2:] 的結果
                    # 2. 匹配 1 個以上：目前首字必須匹配，然後看 s[i+1:] 是否能被目前的 p[j:] 匹配
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    # 沒有 '*'，就是單純的匹配首字，並遞迴看剩下的
                    dp[i][j] = first_match and dp[i+1][j+1]
                    
        # 最終答案在 dp[0][0]
        return dp[0][0]
```
