# 0013 - Roman to Integer (羅馬數字轉整數)

## 1. 題目理解 (Problem Comprehension)

羅馬數字包含以下七種字符：`I`, `V`, `X`, `L`, `C`, `D` 和 `M`。

| 字符 | 數值 |
| :--- | :--- |
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

**規則：**
1.  通常大的數字在左，小的在右，直接相加。
2.  **特例（減法）：** 當較小的符號位在較大的符號左側時，需要減去較小的數值。
    *   `IV` = 5 - 1 = 4
    *   `IX` = 10 - 1 = 9
    *   `XL` = 50 - 10 = 40
    *   `XC` = 100 - 10 = 90
    *   `CD` = 500 - 100 = 400
    *   `CM` = 1000 - 100 = 900

給你一個羅馬數字字串，請將其轉換為整數。

## 2. 思路分析 (Thought Process)

我們只需要遍歷字串，將每個字符對應的數值加起來即可。唯一的挑戰是如何處理那 6 個「減法」特例。

**規律觀察：**
*   在 `III` (3) 中，`I` 後面還是 `I`，相等，所以 `1 + 1 + 1`。
*   在 `IV` (4) 中，`I`(1) 後面是 `V`(5)，**1 小於 5**，所以這是一個減法情況，結果是 `-1 + 5 = 4`。
*   在 `VI` (6) 中，`V`(5) 後面是 `I`(1)，**5 大於 1**，所以是正常的加法，結果是 `5 + 1 = 6`。

**結論：**
對於位置 `i` 的字符，我們看它右邊的字符（位置 `i+1`）：
1.  如果 `value(s[i]) < value(s[i+1])`，則結果要**減去** `value(s[i])`。
2.  否則，結果**加上** `value(s[i])`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **單次遍歷與前瞻比較**。

**偽代碼 (Pseudo-code):**

```text
Function romanToInt(s):
    Initialize map = {'I': 1, 'V': 5, ...}
    Initialize total = 0
    
    For i from 0 to length(s) - 1:
        current_val = map[s[i]]
        
        If i + 1 < length(s) AND current_val < map[s[i+1]]:
            total = total - current_val
        Else:
            total = total + current_val
            
    Return total
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   我們只需要遍歷一次字串 `s`。
*   **空間複雜度 (Space Complexity): O(1)**
    *   雜湊表的大小是固定的（7 個字符），與輸入規模無關。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        # 定義羅馬數字對應的數值對照表
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # 遍歷字串中的每一個字符
        for i in range(n):
            current_val = roman_map[s[i]]
            
            # 關鍵判斷：
            # 如果目前字符的數值小於「下一個」字符的數值，
            # 根據羅馬數字規則，這是一個減法特例（如 IV, IX, XL 等）
            if i + 1 < n and current_val < roman_map[s[i + 1]]:
                # 此時應該減去當前的數值
                total -= current_val
            else:
                # 否則，這是一個正常的加法
                total += current_val
                
        return total
```