# 0026 - Remove Duplicates from Sorted Array (從有序陣列中刪除重複項)

## 1. 題目理解 (Problem Comprehension)

給你一個 **升序排列** 的陣列 `nums` ，請你 **原地 (In-place)** 刪除重複出現的元素，使每個元素 **只出現一次** ，返回刪除後陣列的新長度。

**關鍵要求：**
1.  **原地修改**：不能使用額外的陣列空間，必須直接修改輸入的 `nums`。
2.  **空間複雜度**：必須是 O(1)。
3.  **返回長度**：返回新長度 `k`，且 `nums` 的前 `k` 個元素必須包含原本的所有唯一元素，順序不變。`k` 之後的元素不需要理會。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 有序整數列表。
*   **輸出 (Output):** 新長度 `k` (int)。

**範例：**
輸入: `[1, 1, 2]`
輸出: `2`, `nums` 改為 `[1, 2, _]`

## 2. 思路分析 (Thought Process)

由於陣列是 **已排序** 的，重複的元素一定會相鄰。

**優化思路：快慢雙指針 (Fast and Slow Pointers)**
我們可以用兩個指針來遍歷陣列：
1.  **慢指針 `left`**：指向目前已經處理好的「唯一元素」序列的末尾。
2.  **快指針 `right`**：從左往右掃描整個陣列，尋找新的唯一元素。

**步驟：**
*   一開始，`left` 在索引 0，`right` 從索引 1 開始。
*   如果 `nums[right] == nums[left]`，表示這是重複的，我們不管它，繼續移動 `right`。
*   如果 `nums[right] != nums[left]`，表示我們找到了一個新的唯一元素：
    *   將 `left` 往後移一格 (`left++`)。
    *   把 `right` 找到的這個新元素複製到 `left` 的位置。
*   最後，唯一元素的個數就是 `left + 1`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **雙指針法**。

**偽代碼 (Pseudo-code):**

```text
Function removeDuplicates(nums):
    If nums is empty, return 0
    
    Initialize left = 0
    
    For right from 1 to length(nums) - 1:
        If nums[right] != nums[left]:
            left = left + 1
            nums[left] = nums[right]
            
    Return left + 1
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   其中 N 是陣列的長度。我們只遍歷了陣列一次。
*   **空間複雜度 (Space Complexity): O(1)**
    *   我們只使用了兩個指標變數，沒有使用額外空間。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 如果陣列為空，直接返回長度 0
        if not nums:
            return 0
            
        # 慢指針 left：指向目前最後一個被確認的「唯一元素」
        left = 0
        
        # 快指針 right：從第 1 個元素開始向後掃描
        for right in range(1, len(nums)):
            # 如果快指針發現了一個與慢指針不同的元素
            # 這代表我們找到了一個新的唯一值（因為陣列是有序的）
            if nums[right] != nums[left]:
                # 慢指針往後移一位，準備存放這個新找到的唯一值
                left += 1
                # 將新唯一值覆蓋到慢指針的位置
                nums[left] = nums[right]
                
        # 最終返回唯一元素的總個數
        # 由於 left 是索引（從 0 開始），所以個數是 left + 1
        return left + 1
```
