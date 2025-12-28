# 0028 - Find the Index of the First Occurrence in a String (找出字串中第一個匹配項的下標)

## 1. 題目理解 (Problem Comprehension)

給你兩個字串 `haystack` 和 `needle` ，請你在 `haystack` 字串中找出 `needle` 字串出現的第一個位置（下標從 0 開始）。如果 `needle` 不是 `haystack` 的一部分，則返回 `-1` 。

**輸入與輸出格式：**
*   **輸入 (Input):** `haystack`: 主字串, `needle`: 待尋找的子字串。
*   **輸出 (Output):** 第一個匹配的索引 (int)。

**範例：**
輸入: `haystack = "sadbutsad", needle = "sad"`
輸出: `0`

## 2. 思路分析 (Thought Process)

這道題在傳統電腦科學中被稱為「字串搜索」問題。

### 直觀解法：滑動窗口 (Sliding Window)
我們想像一個長度與 `needle` 相同的窗口，在 `haystack` 上從左往右滑動。
1.  窗口的起點 `i` 從 0 開始，直到 `len(haystack) - len(needle)`。
2.  在每個起點，檢查從 `i` 開始、長度為 `m` 的子串是否等於 `needle`。
3.  如果相等，直接返回 `i`。
4.  如果遍歷完都沒有找到，返回 -1。

### 進階解法：KMP 演算法
雖然滑動窗口足以應付這題，但在面試中，面試官可能會問你如何優化。**KMP (Knuth-Morris-Pratt)** 演算法可以在 O(N) 的時間內完成搜索，它利用了 `needle` 本身的重複特徵來避免不必要的重複比較。不過對於初學者來說，先掌握滑動窗口法是最基礎且重要的。

## 3. 演算法設計 (Algorithm Design)

我們採用 **滑動窗口 (Slicing)**。

**偽代碼 (Pseudo-code):**

```text
Function strStr(haystack, needle):
    If needle is empty, return 0
    
    n = length(haystack)
    m = length(needle)
    
    For i from 0 to n - m:
        # 檢查 haystack 從 i 開始長度為 m 的子串
        If haystack[i...i+m-1] == needle:
            Return i
            
    Return -1
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O((N-M) * M)**
    *   N 是 `haystack` 的長度，M 是 `needle` 的長度。在最壞的情況下（如 `haystack = "aaaaa", needle = "aab"`），我們需要進行多次比較。
*   **空間複雜度 (Space Complexity): O(1)**
    *   在 Python 中，切片 `haystack[i:i+m]` 會產生一個新字串，這在空間上是 O(M)，但我們只是用來比較，不會長期儲存。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 1. 根據題目規範，如果 needle 是空字串，返回 0
        if not needle:
            return 0
            
        n = len(haystack)
        m = len(needle)
        
        # 2. 開始在 haystack 中滑動窗口
        # 迴圈範圍只需到 n - m，因為剩下的長度如果比 needle 短，就不可能匹配
        # +1 是因為 range 不包含結尾
        for i in range(n - m + 1):
            # 3. 提取從 i 開始、長度與 needle 相同的子串
            # 並檢查它是否等於 needle
            # 在 Python 中，字串切片 s[start:end] 非常高效且易讀
            if haystack[i : i + m] == needle:
                # 如果匹配成功，這就是我們要找的第一個出現位置
                return i
                
        # 4. 如果整個迴圈跑完都沒有發現匹配項
        return -1
```
