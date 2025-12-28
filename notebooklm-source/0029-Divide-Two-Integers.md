# 0029 - Divide Two Integers (兩數相除)

## 1. 題目理解 (Problem Comprehension)

給你兩個整數，被除數 `dividend` 和除數 `divisor`。將兩數相除，但**不得使用**乘法、除法和取餘運算子。

返回被除數除以除數得到的商。

**規則：**
1.  整數除法應該向零截斷，也就是說丟棄小數部分。
2.  假設環境只能存儲 32 位元有號整數 `[-2^31, 2^31 - 1]`。
3.  如果除法結果溢出，返回 `2^31 - 1`。

**輸入與輸出格式：**
*   **輸入 (Input):** `dividend`, `divisor` (int)。
*   **輸出 (Output):** 商 (int)。

**範例：**
輸入: `dividend = 10, divisor = 3`
輸出: `3` (10 / 3 = 3.333...，截斷為 3)

## 2. 思路分析 (Thought Process)

不能用乘除法，我們最直覺的想法是用「減法」：看被除數裡面可以減去幾個除數。
但如果 `dividend` 是 21 億，`divisor` 是 1，我們要減 21 億次，這太慢了。

**優化思路：位元運算 (Bit Manipulation)**
我們可以使用「倍增」的思想。與其一個一個減，不如一組一組減。
我們可以利用位元左移 `<<` 來實現乘以 2。

**步驟：**
1.  **處理符號**：記錄結果的正負號，並將兩數轉為正數處理。
2.  **倍增除數**：
    *   假設 `a = 100`, `b = 3`。
    *   `3 << 1 = 6` (3 * 2)
    *   `6 << 1 = 12` (3 * 4)
    *   `12 << 1 = 24` (3 * 8)
    *   `24 << 1 = 48` (3 * 16)
    *   `48 << 1 = 96` (3 * 32)
    *   現在 `96` 很接近 `100` 了。我們從 `100` 中減去 `96`，結果加上 `32`。
    *   剩下 `4`，重複上述過程，`4` 裡面還有一個 `3`，結果加 `1`。
    *   最後結果 `32 + 1 = 33`。
3.  **處理邊界**：確保結果在 32 位元範圍內。

## 3. 演算法設計 (Algorithm Design)

我們採用 **倍增減法 (Exponential Search style)**。

**偽代碼 (Pseudo-code):**

```text
Function divide(dividend, divisor):
    If dividend == MIN and divisor == -1: return MAX
    
    sign = (dividend > 0) == (divisor > 0)
    a = abs(dividend)
    b = abs(divisor)
    res = 0
    
    While a >= b:
        temp_b = b
        multiple = 1
        While a >= (temp_b << 1):
            temp_b = temp_b << 1
            multiple = multiple << 1
            
        a = a - temp_b
        res = res + multiple
        
    Return sign ? res : -res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O((log N)^2)**
    *   外部迴圈減少了 `a`，內部迴圈尋找最大的倍數。這比直接減法快得多。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 定義 32 位元整數的邊界
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        # 特殊情況：溢位處理
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
            
        # 1. 判斷最終結果的正負號
        # 如果兩者同號，結果為正；異號則為負
        is_positive = (dividend > 0) == (divisor > 0)
        
        # 全部轉為正數進行計算
        a, b = abs(dividend), abs(divisor)
        res = 0
        
        # 2. 核心邏輯：使用位移來實現快速減法
        while a >= b:
            # temp_b 會不斷翻倍 (3, 6, 12, 24...)
            # count 也會同步翻倍 (1, 2, 4, 8...)
            temp_b, count = b, 1
            
            # 只要 a 還大於等於 temp_b 的兩倍，就繼續翻倍
            # 這裡的 (temp_b << 1) 相當於 temp_b * 2
            while a >= (temp_b << 1):
                temp_b <<= 1
                count <<= 1
                
            # 減去目前能找到的最大倍數
            a -= temp_b
            # 將對應的商累加到結果
            res += count
            
        # 3. 恢復正負號
        res = res if is_positive else -res
        
        # 4. 最後檢查是否在 32 位元範圍內並返回
        if res < MIN_INT: return MIN_INT
        if res > MAX_INT: return MAX_INT
        return res
```
