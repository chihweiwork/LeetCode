# 0038 - Count and Say (外觀數列)

## 1. 題目理解 (Problem Comprehension)

「外觀數列」是一個整數序列，其生成規則如下：
*   `countAndSay(1) = "1"`
*   `countAndSay(n)` 是對 `countAndSay(n-1)` 的描述，然後轉換成另一個字串。

**如何「描述」一個字串？**
將字串中相鄰且相同的數字進行分組，然後寫下每一組的「個數」和「數字」。
*   `"1"` -> 描述為「一個 1」，寫作 `"11"`。
*   `"11"` -> 描述為「兩個 1」，寫作 `"21"`。
*   `"21"` -> 描述為「一個 2，一個 1」，寫作 `"1211"`。
*   `"1211"` -> 描述為「一個 1，一個 2，兩個 1」，寫作 `"111221"`。

給你一個正整數 `n`，返回外觀數列的第 `n` 項。

**輸入與輸出格式：**
*   **輸入 (Input):** `n`: 正整數 (1 到 30)。
*   **輸出 (Output):** 第 `n` 項字串。

## 2. 思路分析 (Thought Process)

這道題的核心是實現一個「描述 (Say)」函式。我們可以按照題目給出的遞迴定義來處理，或者使用疊代法。

**優化思路：疊代與分組計數**
1.  **初始化**：從 `res = "1"` 開始。
2.  **循環 `n-1` 次**：每次都根據當前的 `res` 生成下一個字串。
3.  **生成下一個字串的方法**：
    *   使用一個指標 `i` 遍歷當前字串。
    *   計算與 `s[i]` 相同的連續字符數量 `count`。
    *   將 `str(count)` 和 `s[i]` 加入新字串。
    *   移動 `i` 到下一組不同的字符開始處。

## 3. 演算法設計 (Algorithm Design)

我們採用 **疊代模擬法**。

**偽代碼 (Pseudo-code):**

```text
Function countAndSay(n):
    res = "1"
    For k from 2 to n:
        res = describe(res)
    Return res

Function describe(s):
    next_s = ""
    i = 0
    While i < length(s):
        count = 1
        While i + 1 < length(s) and s[i] == s[i+1]:
            count++
            i++
        next_s = next_s + str(count) + s[i]
        i++
    Return next_s
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(M)**
    *   其中 M 是數列中所有字串的總長度。雖然難以給出精確的複雜度，但因為 `n` 最大隻到 30，且字串長度增長有限，這個方法非常高效。
*   **空間複雜度 (Space Complexity): O(M)**
    *   需要存儲生成的字串。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        # 1. 基礎情況：第一項是 "1"
        if n == 1:
            return "1"
            
        # 初始項
        res = "1"
        
        # 2. 透過迴圈，從第 1 項推導出第 n 項
        for _ in range(n - 1):
            res = self._get_next(res)
            
        return res
        
    def _get_next(self, s: str) -> str:
        # 輔助函式：根據「外觀」描述規則生成下一個字串
        next_s = [] # 使用列表存儲字串片段，最後再 join，效率比字串直接相加高
        i = 0
        
        while i < len(s):
            # 3. 找出相同字符的連續區塊
            count = 1
            # 只要下一個字符跟目前相同，就繼續增加計數
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            
            # 4. 根據規則，先寫下「個數」，再寫下「數字本身」
            next_s.append(str(count))
            next_s.append(s[i])
            
            # 移到下一個字符
            i += 1
            
        return "".join(next_s)
```
