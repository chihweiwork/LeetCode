# 0003 - Longest Substring Without Repeating Characters (無重複字符的最長子串)

## 1. 題目理解 (Problem Comprehension)

給定一個字串 `s`，請找出其中**不包含重複字符**的**最長子串 (substring)** 的長度。

**輸入與輸出格式：**

*   **輸入 (Input):**
    *   `s`: 一個字串 (可能是空的，也可能包含空格、符號、數字等)。
*   **輸出 (Output):**
    *   一個整數 (int)，代表最長無重複字符子串的長度。

**範例：**
1.  `s = "abcabcbb"` -> 輸出 3 (因為 "abc" 是最長的無重複子串)
2.  `s = "bbbbb"` -> 輸出 1 (因為 "b" 是最長的)
3.  `s = "pwwkew"` -> 輸出 3 (因為 "wke" 是最長的，注意 "pwke" 有重複的 'w'，而且必須是**子串**，不能是子序列)

## 2. 思路分析 (Thought Process)

### 直觀解法：暴力法

最簡單的想法是檢查所有的子串，看看它們是否有重複字符。
*   兩層迴圈產生所有可能的子串 `s[i:j]`。
*   對每個子串檢查是否有重複字符 (可以用 Set)。
*   時間複雜度會達到 O(N^3)，因為子串有 O(N^2) 個，檢查重複又要 O(N)。這在字串很長時會超時。

### 優化思路：滑動窗口 (Sliding Window)

我們可以維護一個「窗口」，這個窗口內的字符保證是**沒有重複**的。
這個窗口由兩個指針定義：`left` (左邊界) 和 `right` (右邊界)。

1.  開始時，`left` 和 `right` 都指向開頭。
2.  我們移動 `right` 指針向右擴展窗口，將新的字符加入。
3.  如果新加入的字符**已經存在**於窗口中（重複了！），我們就需要移動 `left` 指針來縮小窗口，直到把那個重複的字符「移出」窗口為止。
4.  在每一步，我們都記錄當前窗口的大小 `right - left + 1`，並更新最大值。

**如何快速判斷字符是否在窗口中？**
我們可以用一個**雜湊表 (Hash Map)** 來記錄窗口內字符的位置，或者用一個 Set。如果是 Hash Map，我們可以記錄 `{字符: 索引}`。

**優化後的移動策略：**
當我們遇到重複字符 `char` 時，我們不需要一步一步移動 `left`。
如果我們知道上一次 `char` 出現的位置是 `prev_index`，那麼新的 `left` 至少要移動到 `prev_index + 1`，這樣才能避開重複。

## 3. 演算法設計 (Algorithm Design)

我們採用 **滑動窗口 + 雜湊表** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function lengthOfLongestSubstring(s):
    Initialize char_map = {} (Stores char -> index)
    Initialize left = 0
    Initialize max_len = 0

    For right from 0 to length(s) - 1:
        current_char = s[right]

        If current_char is in char_map AND char_map[current_char] >= left:
            # Found a duplicate inside the current window
            # Move left directly to the right of the previous occurrence
            left = char_map[current_char] + 1

        # Update the character's latest index
        char_map[current_char] = right
        
        # Calculate current window length and update max
        max_len = max(max_len, right - left + 1)

    Return max_len
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   我們只遍歷字串一次 (right 指針從頭走到尾)。
    *   left 指針也只會向右移動，不會回頭。
    *   Hash Map 的操作是 O(1)。
*   **空間複雜度 (Space Complexity): O(min(N, M))**
    *   我們需要存儲字符到 Hash Map。M 是字符集的大小（例如 ASCII 是 128，擴展 ASCII 是 256）。
    *   在最壞情況下，空間複雜度取決於字符集的大小，或者字串長度。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 用雜湊表記錄字符最後一次出現的索引
        # 格式: {字符: 索引}
        char_map = {}
        
        # 滑動窗口的左邊界
        left = 0
        
        # 記錄最長長度
        max_len = 0
        
        # right 指針向右遍歷字串
        for right, char in enumerate(s):
            # 如果當前字符已經在 map 中，並且它的位置在當前窗口內 (>= left)
            # 這表示出現了重複字符
            if char in char_map and char_map[char] >= left:
                # 將左邊界直接跳到重複字符的下一位
                # 這樣可以保證窗口內沒有重複的該字符
                left = char_map[char] + 1
            
            # 更新當前字符的索引為最新位置
            char_map[char] = right
            
            # 計算當前窗口長度 (right - left + 1)，並更新最大值
            max_len = max(max_len, right - left + 1)
            
        return max_len
```
