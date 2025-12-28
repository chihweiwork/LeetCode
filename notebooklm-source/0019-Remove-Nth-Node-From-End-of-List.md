# 0019 - Remove Nth Node From End of List (刪除鏈結串列的倒數第 N 個節點)

## 1. 題目理解 (Problem Comprehension)

給你一個鏈結串列，刪除鏈結串列的倒數第 `n` 個節點，並且返回鏈結串列的頭節點。

**輸入與輸出格式：**
*   **輸入 (Input):** `head`: 鏈結串列的頭節點, `n`: 整數（倒數第幾個）。
*   **輸出 (Output):** 刪除節點後的鏈結串列頭節點。

**範例：**
輸入: `1->2->3->4->5`, `n = 2`
輸出: `1->2->3->5` (倒數第 2 個是 4，被刪除了)

**進階要求：**
你能嘗試使用一次遍歷 (One pass) 完成嗎？

## 2. 思路分析 (Thought Process)

### 直觀解法：兩次遍歷
1.  遍歷一次整個串列，算出總長度 `L`。
2.  倒數第 `n` 個節點，就是正數第 `L - n + 1` 個節點。
3.  第二次遍歷到該位置的前一個，進行刪除。

### 優化思路：快慢指針 (Fast and Slow Pointers)
為了在一次遍歷中找到倒數第 `n` 個節點，我們可以使用兩個指針，讓它們之間保持 `n` 的距離。

**步驟：**
1.  建立一個 **啞節點 (Dummy Node)** 指向 `head`。這是一個非常重要的技巧，可以幫我們處理「刪除頭節點」的情況。
2.  讓 `fast` 指針先往前走 `n + 1` 步。
3.  此時 `fast` 和 `slow` 之間隔了 `n` 個節點。
4.  同時移動 `fast` 和 `slow`，直到 `fast` 指向 `None` (走到底)。
5.  此時，`slow` 指針剛好會落在**倒數第 n 個節點的前一個位置**！
6.  執行刪除操作：`slow.next = slow.next.next`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **快慢指針 (一次遍歷)**。

**偽代碼 (Pseudo-code):**

```text
Function removeNthFromEnd(head, n):
    Initialize dummy = new ListNode(0, head)
    Initialize fast = dummy
    Initialize slow = dummy
    
    # 快指針先走 n + 1 步
    For i from 1 to n + 1:
        fast = fast.next
        
    # 同步移動，直到快指針出界
    While fast is not None:
        fast = fast.next
        slow = slow.next
        
    # 刪除目標節點
    slow.next = slow.next.next
    
    Return dummy.next
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(L)**
    *   L 是串列的長度。我們只遍歷了一次串列。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了兩個額外的指針變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import Optional

# 定義單向鏈結串列節點
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. 使用啞節點 (Dummy Node) 是一個好習慣，
        # 它指向 head，可以簡化處理「刪除頭節點」的邏輯
        dummy = ListNode(0, head)
        
        # 2. 初始化快慢指針都指向啞節點
        fast = dummy
        slow = dummy
        
        # 3. 快指針先往前走 n + 1 步
        # 為什麼是 n + 1？因為我們希望 slow 最後停在「被刪除節點」的前一個
        for _ in range(n + 1):
            fast = fast.next
            
        # 4. 同時移動快慢指針
        # 當快指針到達末尾 (None) 時，慢指針剛好在倒數第 n+1 個位置
        while fast:
            fast = fast.next
            slow = slow.next
            
        # 5. 此時 slow.next 就是我們要刪除的那個「倒數第 n 個節點」
        # 將 slow 的 next 跳過目標節點，直接指向下下個
        slow.next = slow.next.next
        
        # 6. 返回啞節點的下一個，即為新的頭節點
        return dummy.next
```
