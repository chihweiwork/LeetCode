# 0030 - Substring with Concatenation of All Words (串聯所有單詞的子串)

## 1. 題目理解 (Problem Comprehension)

這是一道 LeetCode 的 **Hard** 題目。
給你一個字串 `s` 和一個字串陣列 `words`。`words` 中所有字串的**長度都相同**。

一個「串聯子串」是指包含 `words` 中所有字串（以任意順序排列）連接而成的子串，且中間沒有任何其他字符。

請返回 `s` 中所有這類串聯子串的起始索引。

**輸入與輸出格式：**
*   **輸入 (Input):** `s`: 字串, `words`: 字串列表。
*   **輸出 (Output):** 起始索引列表 (List[int])。

**範例：**
`s = "barfoothefoobarman"`, `words = ["foo","bar"]`
輸出: `[0, 9]`
（索引 0 是 "barfoo"，索引 9 是 "foobar"）

## 2. 思路分析 (Thought Process)

這道題的關鍵在於 `words` 中每個單詞的長度 `L` 是固定的。

### 直觀解法：滑動窗口 + 哈希表
我們可以在 `s` 中檢查每一個可能的起點 `i`，看從 `i` 開始長度為 `L * num_words` 的子串是否符合要求。
這需要 O(N * num_words) 的時間，效率稍低。

### 優化思路：移動窗口 (Sliding Window)
既然單詞長度固定為 `L`，我們其實只需要運行 `L` 次滑動窗口。
*   第一次窗口從索引 0 開始，每次移動 `L` 個字符。
*   第二次窗口從索引 1 開始，每次移動 `L` 個字符。
*   ...
*   第 L 次窗口從索引 `L-1` 開始。

在每一次滑動窗口中：
1.  我們用一個 `Counter` 來記錄當前窗口內各個單詞出現的次數。
2.  用一個 `left` 和 `right` 指針來維護窗口。
3.  如果新加入的單詞在 `words` 中：
    *   增加計數。
    *   如果該單詞出現次數超過了 `words` 中的限制，則收縮 `left` 指針直到次數恢復正常。
    *   如果窗口內的單詞總數等於 `num_words`，記錄 `left` 為一個解。
4.  如果新加入的單詞不在 `words` 中：
    *   清空當前計數，將 `left` 移到 `right` 的下一個位置。

## 3. 演算法設計 (Algorithm Design)

我們採用 **多起點滑動窗口**。

**偽代碼 (Pseudo-code):**

```text
Function findSubstring(s, words):
    word_len = length(words[0])
    num_words = length(words)
    word_count = Counter(words)
    res = []
    
    For i from 0 to word_len - 1:
        left = i
        right = i
        current_count = Counter()
        
        While right + word_len <= length(s):
            word = s[right : right + word_len]
            right += word_len
            
            If word in word_count:
                current_count[word]++
                While current_count[word] > word_count[word]:
                    left_word = s[left : left + word_len]
                    current_count[left_word]--
                    left += word_len
                
                If (right - left) / word_len == num_words:
                    Add left to res
            Else:
                current_count.clear()
                left = right
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   其中 N 是字串 `s` 的長度。雖然有 `word_len` 次循環，但每次循環中指針 `left` 和 `right` 都只會遍歷一次字串。
*   **空間複雜度 (Space Complexity): O(M)**
    *   M 是 `words` 的大小，用於儲存哈希表。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
            
        word_len = len(words[0])   # 每個單詞的固定長度
        num_words = len(words)     # 單詞的總個數
        word_count = Counter(words) # 統計 words 中各單詞應有的次數
        res = []
        
        # 為什麼要遍歷 word_len 次？
        # 因為我們的窗口每次跳 word_len，所以要分別從 0, 1, ..., word_len-1 開始
        # 才能覆蓋到所有可能的起始位置
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter() # 記錄目前窗口內的單詞次數
            words_used = 0           # 目前窗口內的總單詞數
            
            # 向右滑動窗口
            while right + word_len <= len(s):
                # 截取一個單詞
                word = s[right : right + word_len]
                right += word_len
                
                # 如果這個單詞在目標 words 列表中
                if word in word_count:
                    current_count[word] += 1
                    words_used += 1
                    
                    # 如果目前的單詞次數超過了規定的次數
                    # 不斷移動左邊界，直到次數恢復正常
                    while current_count[word] > word_count[word]:
                        left_word = s[left : left + word_len]
                        current_count[left_word] -= 1
                        words_used -= 1
                        left += word_len
                    
                    # 如果窗口內的單詞數正好等於總單詞數，說明找到了一個匹配
                    if words_used == num_words:
                        res.append(left)
                else:
                    # 如果遇到一個根本不在 words 列表中的單詞
                    # 之前的努力全白費，清空計數並重置左邊界
                    current_count.clear()
                    words_used = 0
                    left = right
                    
        return res
```
