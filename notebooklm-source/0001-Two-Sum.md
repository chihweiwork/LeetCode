# 0001 - Two Sum (兩數之和)

## 1. 題目理解 (Problem Comprehension)

這道題目要求我們在一個整數陣列 `nums` 中，找出兩個數字，使它們相加的結果等於一個特定的目標值 `target`。

我們需要返回這兩個數字在陣列中的**索引 (index)**。

**輸入與輸出格式：**

*   **輸入 (Input):**
    *   `nums`: 一個整數列表 (List[int])。
    *   `target`: 一個整數 (int)，代表我們想要達到的和。
*   **輸出 (Output):**
    *   一個包含兩個整數的列表 (List[int])，這兩個整數是相加等於 `target` 的那兩個數字的索引。

**限制條件與假設：**
*   每個輸入都**恰好**只有一組解。
*   你不能使用同一個元素兩次（即不能是同一個索引的數字加自己）。
*   返回答案的順序不限。

## 2. 思路分析 (Thought Process)

### 直觀解法：暴力法 (Brute Force)

最直覺的想法是：既然要找兩個數，那我們就用兩層迴圈。
第一層迴圈選定一個數 `x`，第二層迴圈遍歷剩下的數，看看有沒有一個數 `y` 使得 `x + y == target`。

*   **步驟：**
    1.  for `i` from `0` to `length - 1`:
    2.      for `j` from `i + 1` to `length - 1`:
    3.          if `nums[i] + nums[j] == target`:
    4.              return `[i, j]`

*   **分析：**
    *   雖然簡單易懂，但效率很差。
    *   如果有 N 個數字，我們大約要比較 N*N/2 次。
    *   時間複雜度是 O(N^2)，如果陣列很大，執行速度會變得很慢。

### 優化思路：使用雜湊表 (Hash Map)

我們能不能只遍歷一次陣列就找到答案？

當我們看到數字 `x` 時，我們其實是在找陣列中是否存在另一個數字 `y`，使得 `y = target - x`。
問題變成了：**「我有沒有看過 `target - x` 這個數字？如果看過，它的索引在哪裡？」**

這正是**雜湊表 (Hash Map / Dictionary)** 擅長的事情：快速查找鍵值對。

*   **策略：**
    1.  建立一個空的雜湊表 `num_map`，用來儲存 `{數值: 索引}`。
    2.  遍歷陣列中的每一個數字 `num` (索引為 `i`)：
        *   計算我們需要的「另一半」：`complement = target - num`。
        *   檢查 `complement` 是否已經在 `num_map` 裡面？
            *   **是**：找到了！目前的 `num` 和之前的 `complement` 加起來就是 `target`。直接返回 `[num_map[complement], i]`。
            *   **否**：把目前的 `num` 和它的索引 `i` 存入 `num_map`，供後面的數字查找。

這個方法只需要遍歷陣列一次，而且雜湊表的查找平均是 O(1) 的時間。

## 3. 演算法設計 (Algorithm Design)

我們採用 **雜湊表 (Hash Map)** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function twoSum(nums, target):
    Initialize an empty map: num_map

    For each index i, value num in nums:
        Calculate complement = target - num

        If complement exists in num_map:
            Return [num_map[complement], i]

        Store num in num_map with value i: num_map[num] = i

    Return empty list (though problem guarantees a solution)
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   我們只遍歷了陣列一次 (N 個元素)。
    *   在雜湊表中進行查找和插入操作的平均時間複雜度是 O(1)。
    *   所以總時間是 O(N)。
*   **空間複雜度 (Space Complexity): O(N)**
    *   在最壞的情況下（例如直到最後兩個數字才找到答案），我們需要將幾乎所有的元素都存入雜湊表中，所以需要 O(N) 的額外空間。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 建立一個空的字典 (Hash Map) 用來儲存看過的數字和它們的索引
        # 格式: {數值: 索引}
        num_map = {}
        
        # 使用 enumerate 同時取得索引 (i) 和數值 (num)
        for i, num in enumerate(nums):
            # 計算我們需要的「另一半」數字 (complement)
            # 因為 num + complement = target
            complement = target - num
            
            # 檢查這個 complement 是否已經在我們的字典裡出現過
            # 如果在，代表我們之前已經遍歷過這個數字了
            if complement in num_map:
                # 找到了！
                # num_map[complement] 是之前那個數字的索引
                # i 是目前這個數字 (num) 的索引
                return [num_map[complement], i]
            
            # 如果還沒找到配對，就將目前的數字和索引存入字典
            # 這樣未來的數字就可以查找到目前的數字
            num_map[num] = i
            
        # 題目保證一定有解，所以理論上不會執行到這裡，
        # 但為了程式碼完整性，可以返回一個空列表
        return []
```
