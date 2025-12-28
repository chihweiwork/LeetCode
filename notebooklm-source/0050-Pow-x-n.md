# 0050 - Pow(x, n) (x 的 n 次冪)

## 1. 題目理解 (Problem Comprehension)

實現 `pow(x, n)` ，即計算 `x` 的 `n` 次冪函數（即 x^n）。

**輸入與輸出格式：**
*   **輸入 (Input):** `x`: 浮點數 (float), `n`: 整數 (int)。
*   **輸出 (Output):** `x^n` 的結果 (float)。

**範例：**
輸入: `x = 2.00000, n = 10` -> 輸出: `1024.00000`
輸入: `x = 2.00000, n = -2` -> 輸出: `0.25000`

## 2. 思路分析 (Thought Process)

最直覺的方法是將 `x` 連乘 `n` 次。
*   如果 `n = 10^9`，連乘 10 億次會太慢 (O(N))。
*   我們需要一種更高效的方法。

**優化思路：快速冪演算法 (Fast Power / Binary Exponentiation)**
利用「分治法」的思想：
*   如果我要算 `x^10`，我可以先算出 `x^5`，然後再把結果平方：`x^10 = (x^5)^2`。
*   如果我要算 `x^5`，我可以先算出 `x^2`，然後：`x^5 = x * (x^2)^2`。

這樣，我們每次都能將指數減少一半，計算次數會從 O(N) 降低到 **O(log N)**。

**處理負指數：**
*   根據數學規則：`x^(-n) = (1/x)^n`。
*   我們可以先將 `x` 變為 `1/x`，並將 `n` 變為正數，然後套用同樣的快速冪邏輯。

## 3. 演算法設計 (Algorithm Design)

我們採用 **遞迴式的快速冪**。

**偽代碼 (Pseudo-code):**

```text
Function myPow(x, n):
    If n == 0: Return 1
    If n < 0:
        x = 1 / x
        n = -n
        
    Function fast_pow(x, n):
        If n == 0: Return 1
        
        half = fast_pow(x, n / 2)
        
        If n is even:
            Return half * half
        Else:
            Return half * half * x
            
    Return fast_pow(x, n)
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(log N)**
    *   每次遞迴指數都減半。
*   **空間複雜度 (Space Complexity): O(log N)**
    *   遞迴堆疊的深度。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1. 基礎情況：任何數的 0 次方都是 1
        if n == 0:
            return 1.0
            
        # 2. 處理負指數情況
        # x^(-n) 等於 (1/x) 的 n 次方
        if n < 0:
            x = 1 / x
            n = -n
            
        # 3. 定義快速冪的輔助遞迴函式
        def fast_pow(base, exp):
            # 遞迴終止條件
            if exp == 0:
                return 1.0
            
            # 核心：先算出指數一半的結果
            # 這樣我們只需要算一次，然後平方它即可
            half = fast_pow(base, exp // 2)
            
            # 如果指數是偶數，例如 x^10 = (x^5) * (x^5)
            if exp % 2 == 0:
                return half * half
            # 如果指數是奇數，例如 x^11 = (x^5) * (x^5) * x
            else:
                return half * half * base
                
        # 開始執行快速冪計算
        return fast_pow(x, n)
```
