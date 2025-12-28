# 0049 - Group Anagrams (字母異位詞分組)

## 1. 題目理解 (Problem Comprehension)

給你一個字串陣列 `strs` ，請你將 **字母異位詞 (Anagrams)** 組合在一起。可以按任意順序返回結果列表。

**字母異位詞** 是指由同樣的字母組成的不同單詞。換句話說，如果兩個單詞包含的字母及其頻率都完全相同，只是順序不同，它們就是字母異位詞。

**輸入與輸出格式：**
*   **輸入 (Input):** `strs`: 字串列表。
*   **輸出 (Output):** 字串列表的列表 (List[List[str]])。

**範例：**
輸入: `["eat", "tea", "tan", "ate", "nat", "bat"]`
輸出: `[["bat"],["nat","tan"],["ate","eat","tea"]]`

## 2. 思路分析 (Thought Process)

問題在於：**如何判斷兩個字串是字母異位詞，並快速將它們歸類？**

如果兩個字串是字母異位詞，它們一定有一個共同的「特徵」。

**方法一：排序後作為鍵 (Sorting)**
字母異位詞排序後的結果是完全一樣的。
*   `"eat"` -> 排序為 `"aet"`
*   `"tea"` -> 排序為 `"aet"`
*   `"ate"` -> 排序為 `"aet"`
這就是我們要的共同特徵。我們可以用一個雜湊表 (Dictionary) 來儲存：
*   鍵 (Key): 排序後的字串。
*   值 (Value): 屬於該類別的原始字串列表。

**方法二：字元計數作為鍵 (Counting)**
如果不排序，也可以統計每個字母出現的次數（a-z 總共 26 個）。將這 26 個次數組成一個元組 (tuple) 作為鍵。這在某些情況下會更快，但方法一在 Python 中實作最簡潔。

## 3. 演算法設計 (Algorithm Design)

我們採用 **排序 + 雜湊表** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function groupAnagrams(strs):
    Initialize map = empty dictionary
    
    For each s in strs:
        # 將字串排序，作為特徵鍵
        key = join(sort(s))
        
        If key not in map:
            map[key] = [s]
        Else:
            map[key].append(s)
            
    Return list of all values in map
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N * K log K)**
    *   N 是字串個數，K 是單個字串的最大長度。每個字串都需要進行一次排序。
*   **空間複雜度 (Space Complexity): O(N * K)**
    *   需要雜湊表來存儲所有的字串。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. 建立一個字典，用來存放分組後的結果
        # 使用 defaultdict(list) 的好處是：當鍵不存在時，會自動建立一個空列表
        anagram_map = defaultdict(list)
        
        # 2. 遍歷輸入的每一個字串
        for s in strs:
            # 3. 核心邏輯：將字串中的字母進行排序
            # 例如 "eat" -> ['a', 'e', 't'] -> "aet"
            # 只要是字母組成相同的單詞，排序後的字串一定是一模一樣的
            sorted_s = "".join(sorted(s))
            
            # 4. 將原始字串加入對應特徵鍵的列表中
            anagram_map[sorted_s].append(s)
            
        # 5. 返回字典中所有的值（即所有的分組列表）
        return list(anagram_map.values())
```
