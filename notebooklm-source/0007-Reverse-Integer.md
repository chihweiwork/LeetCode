# 0007 - Reverse Integer (整數反轉)

## 1. 題目理解 (Problem Comprehension)

給你一個 32 位元的有號整數 `x`，請你將這個整數中每一位數字進行反轉。

**特別注意：**
如果反轉後的整數超過了 32 位元有號整數的範圍 `[-2^31, 2^31 - 1]`，則返回 0。

**輸入與輸出格式：**
*   **輸入 (Input):** `x` (int)
*   **輸出 (Output):** 反轉後的整數 (int)，若溢位則為 0。

**範例：**
*   `123` -> `321`
*   `-123` -> `-321`
*   `120` -> `21`

## 2. 思路分析 (Thought Process)

### 如何反轉數字？

我們可以用數學的方法，不斷地取「個位數」並將它加到新數字的末尾。

1.  準備一個 `res = 0`。
2.  取出 `x` 的個位數：`pop = x % 10`。
3.  將 `res` 往左移一位並加上 `pop`：`res = res * 10 + pop`。
4.  將 `x` 去掉個位數：`x = x // 10`。
5.  重複上述步驟直到 `x` 變為 0。

### 處理負數與溢位

*   **負數**：在 Python 中，對負數取餘數 (`%`) 和地板除法 (`//`) 的行為可能與其他語言（如 C++ 或 Java）不同。為了簡單起見，我們可以先處理 `x` 的絕對值，記錄符號，最後再乘回去。
*   **溢位**：題目明確要求我們考慮 32 位元限制。反轉完成後，檢查結果是否落在 `[-2147483648, 2147483647]` 之間。

## 3. 演算法設計 (Algorithm Design)

我們採用 **數學取餘法**。

**偽代碼 (Pseudo-code):**

```text
Function reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    res = 0
    
    While x > 0:
        digit = x % 10
        res = res * 10 + digit
        x = x // 10
        
    res = res * sign
    
    If res < -2^31 or res > 2^31 - 1:
        Return 0
        
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(log10(x))**
    *   數字 `x` 大約有 `log10(x)` 位數字，我們迴圈的次數等於位數。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def reverse(self, x: int) -> int:
        # 記錄符號，並將 x 轉為正數處理，避免 Python 負數取餘數的特殊行為
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        
        # 當 x 還大於 0 時，繼續取出最後一位數字
        while x != 0:
            # 取出最後一位數字 (個位)
            digit = x % 10
            # 將目前結果乘以 10 (左移一位)，再加上取出的數字
            res = res * 10 + digit
            # 去掉 x 的最後一位數字
            x //= 10
            
        # 將原本的符號補回來
        res *= sign
        
        # 檢查是否超出 32 位元有號整數範圍 [-2^31, 2^31 - 1]
        # -2^31 = -2147483648
        # 2^31 - 1 = 2147483647
        if res < -2**31 or res > 2**31 - 1:
            return 0
            
        return res
```
