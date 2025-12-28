# 0021 - Merge Two Sorted Lists (合併兩個有序鏈結串列)

## 1. 題目理解 (Problem Comprehension)

將兩個升序鏈結串列合併為一個新的 **升序** 鏈結串列。新串列是通過拼接給定的兩個串列的所有節點組成的。

**輸入與輸出格式：**
*   **輸入 (Input):** `list1`, `list2`: 兩個已排序的鏈結串列頭節點。
*   **輸出 (Output):** 合併後的有序鏈結串列頭節點。

**範例：**
輸入: `1->2->4`, `1->3->4`
輸出: `1->1->2->3->4->4`

## 2. 思路分析 (Thought Process)

這道題非常直觀，就像是在玩兩疊已經排好序的撲克牌，我們每次從兩疊牌的最上面選一張較小的，放到新的牌堆裡。

**優化思路：疊代法 (Iterative)**
1.  建立一個 **啞節點 (Dummy Node)** 作為結果串列的開頭，方便操作。
2.  使用一個指針 `curr` 指向結果串列的當前末尾。
3.  比較 `list1` 和 `list2` 當前節點的值：
    *   如果 `list1.val <= list2.val`，將 `list1` 接到 `curr.next`，並移動 `list1`。
    *   否則，將 `list2` 接到 `curr.next`，並移動 `list2`。
4.  移動 `curr` 指針。
5.  重複上述步驟直到其中一個串列為空。
6.  **收尾**：將剩餘不為空的那個串列直接接到 `curr.next`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **疊代法**。

**偽代碼 (Pseudo-code):**

```text
Function mergeTwoLists(list1, list2):
    Initialize dummy = new ListNode(0)
    Initialize curr = dummy
    
    While list1 is not None AND list2 is not None:
        If list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        Else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
        
    If list1 is not None:
        curr.next = list1
    Else:
        curr.next = list2
        
    Return dummy.next
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N + M)**
    *   N 和 M 分別是兩個鏈結串列的長度。我們需要遍歷兩個串列的所有節點。
*   **空間複雜度 (Space Complexity): O(1)**
    *   我們只是改變了現有節點的指標指向，沒有使用額外的節點空間（除了啞節點）。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import Optional

# 定義單向鏈結串列節點
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 建立一個啞節點 (Dummy Node)，作為合併後串列的起點
        dummy = ListNode(0)
        # curr 指針用來追蹤目前合併到哪一個節點了
        curr = dummy
        
        # 2. 當兩個串列都還有節點時，進行比較
        while list1 and list2:
            if list1.val <= list2.val:
                # 如果 list1 的值較小或相等，將 list1 的節點接上去
                curr.next = list1
                # list1 往後移一步
                list1 = list1.next
            else:
                # 否則將 list2 的節點接上去
                curr.next = list2
                # list2 往後移一步
                list2 = list2.next
            
            # 每接上一個節點，curr 指針也要往後移
            curr = curr.next
            
        # 3. 迴圈結束後，可能其中一個串列還剩下一些節點
        # 因為串列原本就是有序的，我們直接把剩餘的部分接在最後面即可
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
            
        # 4. 返回啞節點的下一個節點，即為合併後真正的頭節點
        return dummy.next
```
