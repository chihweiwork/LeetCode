# 0012 - Integer to Roman (整數轉羅馬數字)

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
1.  一般情況下，較大的數字在左邊，相加得到結果（如 `XII` = 12）。
2.  **特例（減法）：**
    *   `I` 在 `V`(5) 或 `X`(10) 之前，表示 4 或 9。
    *   `X` 在 `L`(50) 或 `C`(100) 之前，表示 40 或 90。
    *   `C` 在 `D`(500) 或 `M`(1000) 之前，表示 400 或 900。

給你一個 1 到 3999 之間的整數，請將其轉換為羅馬數字。

## 2. 思路分析 (Thought Process)

這道題可以看作是一個「找零錢」的問題。我們有一堆不同面值的羅馬數字（包含特例），我們想用盡可能大的面值去組合出目標數字。

**策略：**
1.  將所有基本的羅馬數字和 6 個特例按**從大到小**列出來。
2.  從最大的面值 (1000, 'M') 開始，看目前的 `num` 裡面包含幾個這個面值。
3.  將對應數量的符號加入結果字串，並從 `num` 中減去對應的數值。
4.  移向下一種面值，重複直到 `num` 變為 0。

## 3. 演算法設計 (Algorithm Design)

我們採用 **貪心演算法 (Greedy Algorithm)**。

**偽代碼 (Pseudo-code):**

```text
Function intToRoman(num):
    Define pairs = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    
    Initialize result = ""
    
    For value, symbol in pairs:
        While num >= value:
            num = num - value
            result = result + symbol
            
    Return result
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(1)**
    *   雖然看起來有個迴圈，但由於 `num` 的最大值被限制在 3999，且羅馬數字的符號數量是固定的常數。
*   **空間複雜度 (Space Complexity): O(1)**
    *   儲存對應關係的空間是固定的。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        # 建立一個清單，包含所有的羅馬數字基礎值和特殊減法情況
        # 順序必須從大到小，這樣我們才能實施「貪心」策略
        value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        
        res = []
        
        # 遍歷所有的面值
        for value, symbol in value_map:
            # 如果剩餘的數字已經是 0，可以提早結束
            if num == 0:
                break
            
            # 使用 divmod 同時取得商數 (count) 和餘數 (num)
            # count 代表 num 裡面可以塞進幾個當前面值
            count, num = divmod(num, value)
            
            # 將該符號重複對應次數並加入結果清單
            # Python 中字串乘以數字可以重複字串，例如 'M' * 3 = 'MMM'
            res.append(symbol * count)
            
        # 最後將所有字串片段拼接起來
        return "".join(res)
```