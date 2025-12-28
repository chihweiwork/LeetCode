# 0023 - Merge k Sorted Lists (合併 k 個有序鏈結串列)

## 1. 題目理解 (Problem Comprehension)

給你一個鏈結串列陣列，每個鏈結串列都已經按升序排列。請將所有鏈結串列合併到一個升序鏈結串列中，返回合併後的鏈結串列。

這是一道 LeetCode 的 **Hard** 題目，是「合併兩個有序串列」的擴展版。

**輸入與輸出格式：**
*   **輸入 (Input):** `lists`: 一個包含多個有序鏈結串列頭節點的列表。
*   **輸出 (Output):** 合併後的一個有序鏈結串列。

**範例：**
輸入: `[[1,4,5],[1,3,4],[2,6]]`
輸出: `[1,1,2,3,4,4,5,6]`

## 2. 思路分析 (Thought Process)

我們有多個已經排好序的串列，每次都想從所有串列的「當前頭節點」中選出一個最小的。

### 方法一：分治法 (Divide and Conquer)
就像歸併排序一樣，兩兩合併。
*   先把 `k` 個串列分成兩半，分別合併，最後再把這兩個大串列合併。
*   時間複雜度：O(N log k)，其中 N 是總節點數。

### 方法二：優先權隊列 / 堆積 (Priority Queue / Heap) - **推薦**
我們維護一個「最小堆積 (Min-Heap)」，裡面存放所有串列的當前頭節點。
1.  將 `k` 個串列的頭節點都放入堆積。
2.  每次從堆積中彈出 (pop) 最小的節點，將它接到結果串列後。
3.  如果彈出的節點還有下一個節點 (`node.next`)，則將下一個節點放入堆積。
4.  重複直到堆積為空。

**為什麼推薦方法二？**
在 Python 中使用 `heapq` 非常方便，且這種思路可以很好地擴展到「處理超大數據（無法一次全部放入內存）」的情境。

## 3. 演算法設計 (Algorithm Design)

我們採用 **最小堆積 (Min-Heap)** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function mergeKLists(lists):
    Initialize min_heap = []
    
    # 將每個非空串列的頭節點放入堆積
    For each head in lists:
        If head is not None:
            Push (head.val, head) to min_heap
            
    Initialize dummy = new ListNode(0)
    Initialize curr = dummy
    
    While min_heap is not None:
        val, node = Pop min_heap
        curr.next = node
        curr = curr.next
        
        If node.next is not None:
            Push (node.next.val, node.next) to min_heap
            
    Return dummy.next
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N log k)**
    *   N 是所有串列的總節點數。每次插入或刪除堆積的操作是 O(log k)，總共執行 N 次。
*   **空間複雜度 (Space Complexity): O(k)**
    *   堆積的大小最多同時存儲 `k` 個節點。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List, Optional
import heapq

# 定義單向鏈結串列節點
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 建立一個最小堆積 (Min-Heap)
        min_heap = []
        
        # 1. 初始化堆積：將每個鏈結串列的頭節點加入堆積中
        # 我們加入 (head.val, i, head) 而不是 (head.val, head)
        # 是因為如果 val 相等，Python 會嘗試比較 ListNode 物件，
        # 而 ListNode 沒有定義比較運算子會噴錯。i (索引) 可以作為第二層比較。
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))
        
        dummy = ListNode(0)
        curr = dummy
        
        # 2. 只要堆積不為空，就不斷取出最小的節點
        while min_heap:
            # 彈出當前所有串列中最小的那個節點
            val, i, node = heapq.heappop(min_heap)
            
            # 將該節點接到結果串列
            curr.next = node
            curr = curr.next
            
            # 3. 關鍵：如果被彈出的節點還有下一個節點，將下一個節點加入堆積
            # 這保證了堆積中始終包含每個串列中「目前最小」的候選人
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        # 返回合併後的串列起點
        return dummy.next
```
