# 0004 - Median of Two Sorted Arrays (尋找兩個正序陣列的中位數)

## 1. 題目理解 (Problem Comprehension)

這是一道 LeetCode 中標記為 **Hard** 的題目。
給定兩個大小分別為 `m` 和 `n` 的**正序（從小到大排序）**陣列 `nums1` 和 `nums2`。
請你找出這兩個陣列合併後的中位數 (Median)。

**輸入與輸出格式：**

*   **輸入 (Input):**
    *   `nums1`: 一個排序好的整數列表 (List[int])。
    *   `nums2`: 另一個排序好的整數列表 (List[int])。
*   **輸出 (Output):**
    *   一個浮點數 (float)，代表中位數。

**要求：**
*   演算法的時間複雜度必須是 **O(log (m+n))**。這是一個非常強的提示，意味著我們不能將兩個陣列合併後再找中位數（因為合併是 O(m+n)）。我們必須使用二分搜尋 (Binary Search)。

## 2. 思路分析 (Thought Process)

### 直觀解法：合併後查找 (Merge and Find)

最直觀的想法是新建一個陣列，將 `nums1` 和 `nums2` 按順序合併進去，然後直接取中間的數。
*   合併過程類似「歸併排序」的合併步驟，時間複雜度是 O(m+n)。
*   雖然能解出來，但不符合題目 O(log (m+n)) 的要求。

### 優化思路：二分搜尋 (Binary Search)

要達到 O(log (m+n))，我們必須在不合併的情況下找到中位數。
中位數的定義是：將一組數分成兩半，左半邊的所有數都小於等於右半邊的所有數。

我們可以想像把 `nums1` 和 `nums2` 分別切成兩半：
`nums1` 切在位置 `i`： `nums1[0...i-1]` | `nums1[i...m-1]`
`nums2` 切在位置 `j`： `nums2[0...j-1]` | `nums2[j...n-1]`

我們希望能找到一個切分點，使得：
1.  **左邊的總個數**等於（或比右邊多一個）總數的一半。
2.  **左邊的所有元素 <= 右邊的所有元素**。
    *   具體來說，就是 `nums1[i-1] <= nums2[j]` 且 `nums2[j-1] <= nums1[i]`。

如果滿足這兩個條件，那麼中位數就可以從這四個邊界值 (`nums1[i-1]`, `nums2[j-1]`, `nums1[i]`, `nums2[j]`) 算出來。

因為 `i` 和 `j` 是有關聯的（總個數固定），我們只需要對較短的那個陣列進行二分搜尋來決定 `i` 的位置，`j` 就可以自動算出。

## 3. 演算法設計 (Algorithm Design)

我們選擇對長度較短的陣列（假設是 `nums1`）進行二分搜尋。

1.  確保 `len(nums1) <= len(nums2)`。如果不是，就交換它們。
2.  在 `[0, m]` 的範圍內二分搜尋 `i`（`nums1` 的切分點）。
3.  計算 `nums2` 的切分點 `j = (m + n + 1) // 2 - i`。
    *   這裡 `(m + n + 1) // 2` 是為了處理總數是奇數的情況，讓左半邊多一個元素。
4.  檢查邊界條件：
    *   如果 `nums1[i-1] > nums2[j]`：表示 `i` 太大了（`nums1` 左邊太大），需要往左移 (`high = i - 1`)。
    *   如果 `nums2[j-1] > nums1[i]`：表示 `i` 太小了（`nums2` 左邊太大，應該讓 `nums1` 分擔更多小的數），需要往右移 (`low = i + 1`)。
    *   否則：找到了正確的切分點！

5.  找到切分點後，計算中位數：
    *   左半邊的最大值 `maxLeft = max(nums1[i-1], nums2[j-1])` (注意邊界處理，如果是 0 則設為負無窮)。
    *   如果總數是奇數，中位數就是 `maxLeft`。
    *   如果總數是偶數，還需要右半邊的最小值 `minRight = min(nums1[i], nums2[j])` (注意邊界處理，如果是 m 或 n 則設為正無窮)。
    *   中位數是 `(maxLeft + minRight) / 2`。

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(log(min(m, n)))**
    *   我們只對較短的陣列進行二分搜尋。
*   **空間複雜度 (Space Complexity): O(1)**
    *   我們只使用了幾個變數來存儲索引和邊界值，不需要額外空間。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 確保 nums1 是較短的那個陣列，這樣可以優化二分搜尋的效率
        # 並且避免 j 計算出來是負數的情況
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            # partitionX 是 nums1 的切分點 (即 i)
            partitionX = (low + high) // 2
            # partitionY 是 nums2 的切分點 (即 j)
            # (m + n + 1) // 2 確保左半邊的元素總數等於右半邊 (偶數時) 或多一個 (奇數時)
            partitionY = (m + n + 1) // 2 - partitionX
            
            # 處理邊界情況：如果切分點在最左邊，左邊值設為負無窮
            # 如果切分點在最右邊，右邊值設為正無窮
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            
            # 檢查是否滿足交叉小於等於的條件
            # nums1 左邊 <= nums2 右邊  且  nums2 左邊 <= nums1 右邊
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # 找到了正確的切分點！
                
                # 如果總元素個數是偶數
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    # 如果是奇數，中位數就是左半邊最大的那個數
                    return max(maxLeftX, maxLeftY)
            
            # 如果 nums1 左邊太大，表示切分點太靠右，需要左移
            elif maxLeftX > minRightY:
                high = partitionX - 1
            # 如果 nums2 左邊太大 (即 nums1 右邊太小)，表示切分點太靠左，需要右移
            else:
                low = partitionX + 1
        
        # 理論上不會執行到這裡，因為輸入保證是排序好的陣列
        raise ValueError("Input arrays are not sorted or invalid.")
```
