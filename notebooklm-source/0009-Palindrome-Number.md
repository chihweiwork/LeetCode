# 0009 - Palindrome Number (迴文數)

## 1. 題目理解 (Problem Comprehension)

給你一個整數 `x`，如果 `x` 是一個迴文整數，返回 `true`；否則，返回 `false`。

迴文數是指正序（從左向右）和倒序（從右向左）讀都是一樣的整數。

**輸入與輸出格式：**
*   **輸入 (Input):** `x` (int)
*   **輸出 (Output):** `True` 或 `False` (bool)

**範例：**
*   `121` -> `True`
*   `-121` -> `False` (從右向左讀為 `121-`，不相等)
*   `10` -> `False` (從右向左讀為 `01`)

**進階挑戰：**
你能不將整數轉為字串來解決這個問題嗎？

## 2. 思路分析 (Thought Process)

### 直觀解法：轉為字串

最簡單的方法是把數字轉成字串，然後檢查字串是否跟反轉後的自己相等。
但在面試中，面試官通常希望你用數學方法解決，不使用字串轉換。

### 優化思路：反轉一半數字

我們可以參考「反轉整數」的做法，但為了避免反轉後數字太大造成溢位（雖然 Python 不會溢位，但在其他語言會），我們只需要**反轉一半**的數字。

**核心邏輯：**
1.  **排除明顯不符合的情況**：
    *   負數一定不是迴文。
    *   如果數字最後一位是 0，除非該數字就是 0，否則一定不是迴文（因為開頭不會是 0）。
2.  **反轉後一半**：
    *   將數字 `x` 的後半段反轉成 `reversed_half`。
    *   如何知道已經反轉到一半了？當 `x` 變得小於或等於 `reversed_half` 時。
3.  **比較**：
    *   如果數字位數是偶數（如 1221），則 `x == reversed_half` (12 == 12)。
    *   如果數字位數是奇數（如 121），最後會變成 `x = 1`, `reversed_half = 12`。此時中間的數字不影響迴文，所以我們比較 `x == reversed_half // 10` (1 == 1)。

## 3. 演算法設計 (Algorithm Design)

我們採用 **反轉一半數字** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function isPalindrome(x):
    # 排除特殊情況
    If x < 0 OR (x % 10 == 0 AND x != 0):
        Return False
    
    Initialize reversed_half = 0
    While x > reversed_half:
        # 取出 x 的最後一位並加入 reversed_half
        reversed_half = reversed_half * 10 + (x % 10)
        x = x // 10
        
    # 當長度為奇數時，藉由 reversed_half // 10 去掉中間位數
    Return x == reversed_half OR x == reversed_half // 10
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(log10(x))**
    *   我們只處理了數字的一半位數，所以時間是 O(log10(x) / 2)，簡化為 O(log10(x))。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只需要常數個變數儲存反轉後的數字。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 排除所有負數，以及最後一位是 0 的正整數（因為第一位不可能為 0，除非是 0 本身）
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        # 將數字 x 的後半段取出並反轉
        # 當 x <= reversed_half 時，表示我們已經處理到中間位置了
        while x > reversed_half:
            # 取出 x 的個位數
            last_digit = x % 10
            # 將這個數字加到反轉變數中
            reversed_half = reversed_half * 10 + last_digit
            # 將 x 的最後一位移除
            x //= 10
            
        # 如果數字是偶數位數（例如 1221），最後 x=12, reversed_half=12
        # 如果數字是奇數位數（例如 121），最後 x=1, reversed_half=12
        # 在奇數情況下，中間的數字 2 被存在 reversed_half 的個位，
        # 我們可以用 reversed_half // 10 把這個中間位去掉，再跟 x 比較
        return x == reversed_half or x == reversed_half // 10
```