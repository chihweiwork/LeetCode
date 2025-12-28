# 0027 - Remove Element (移除元素)

## 1. 題目理解 (Problem Comprehension)

給你一個陣列 `nums` 和一個值 `val`，你需要 **原地 (In-place)** 移除所有數值等於 `val` 的元素，並返回移除後陣列的新長度。

**關鍵要求：**
1.  **原地修改**：不能使用額外的陣列空間。
2.  **元素順序**：元素的順序可以改變。
3.  **返回長度**：返回新長度 `k`，`nums` 的前 `k` 個元素不能包含 `val`。`k` 之後的元素不重要。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 整數列表, `val`: 要移除的目標值。
*   **輸出 (Output):** 新長度 `k` (int)。

**範例：**
輸入: `nums = [3, 2, 2, 3], val = 3`
輸出: `2`, `nums` 改為 `[2, 2, _, _]`

## 2. 思路分析 (Thought Process)

由於題目說「順序可以改變」，這給了我們一個優化的空間：當我們發現一個要刪除的元素時，我們不需要把後面的元素全部往前挪（那樣是 O(N^2)），我們只需要把**最後一個元素**搬過來覆蓋它即可。

**優化思路：雙指針 (左右夾擊)**
我們使用兩個指針：
1.  `left`：從左往右掃描。
2.  `right`：指向陣列的當前「邏輯末尾」。

**步驟：**
*   遍歷 `left` 指針：
    *   如果 `nums[left] == val`：
        *   這是一個要被刪除的數字。
        *   我們把陣列最後一個數字 `nums[right-1]` 搬到 `nums[left]` 的位置。
        *   然後縮小陣列範圍 (`right--`)。
        *   **注意**：搬過來的數字可能也是 `val`，所以下一輪我們不移動 `left`，而是繼續檢查目前的 `nums[left]`。
    *   如果 `nums[left] != val`：
        *   這是一個要保留的數字，我們放心地把 `left` 往後移一格。
*   最後，`right` 就是新陣列的長度。

## 3. 演算法設計 (Algorithm Design)

我們採用 **雙指針法 (交換末尾)**。

**偽代碼 (Pseudo-code):**

```text
Function removeElement(nums, val):
    left = 0
    right = length(nums)
    
    While left < right:
        If nums[left] == val:
            # 用最後一個元素覆蓋目前的元素
            nums[left] = nums[right - 1]
            # 縮小有效範圍
            right = right - 1
        Else:
            # 不是要刪除的，繼續看下一個
            left = left + 1
            
    Return right
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   其中 N 是陣列的長度。在最壞的情況下，每個元素最多被訪問一次。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # left: 目前正在檢查的元素位置
        # right: 目前陣列的「有效長度」邊界
        left, right = 0, len(nums)
        
        while left < right:
            # 如果發現目前的數字是要刪除的目標值
            if nums[left] == val:
                # 技巧：將陣列最後一個元素 (right - 1) 搬過來覆蓋它
                # 因為題目說順序不重要，這樣可以省去搬移所有後續元素的麻煩
                nums[left] = nums[right - 1]
                
                # 有效長度減 1
                right -= 1
                
                # 注意：這裡「不移動」left 指針
                # 因為剛從後面搬過來的那個數字，還沒被檢查過是否等於 val
            else:
                # 如果目前的數字不是 val，則安全通過，移動到下一個
                left += 1
                
        # 最後 right 指針所代表的就是剩餘元素的個數
        return right
```
