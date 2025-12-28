# 0024 - Swap Nodes in Pairs (兩兩交換鏈結串列中的節點)

## 1. 題目理解 (Problem Comprehension)

給你一個鏈結串列，兩兩交換其中相鄰的節點，並返回交換後的鏈結串列。

**注意：**
*   你不能只是單純地改變節點內部的值，而是需要實際進行**節點指標 (Pointer)** 的交換。
*   如果最後剩下一個孤單的節點，則保持原樣。

**輸入與輸出格式：**
*   **輸入 (Input):** `head`: 鏈結串列頭節點。
*   **輸出 (Output):** 交換後的頭節點。

**範例：**
輸入: `1->2->3->4`
輸出: `2->1->4->3`

## 2. 思路分析 (Thought Process)

這是一道基礎的鏈結串列操作題。重點在於如何處理指標的指向關係，而不丟失串列的其餘部分。

**優化思路：疊代法 + 啞節點 (Iterative with Dummy Node)**
1.  建立一個 **啞節點 (Dummy Node)** 指向 `head`。這可以幫我們輕鬆處理原頭節點 (1 和 2) 被交換後，頭節點變成 2 的情況。
2.  使用一個指針 `prev` 指向每一對要交換的節點的前一個位置（初始為啞節點）。
3.  每次迴圈處理 `prev.next` (first) 和 `prev.next.next` (second)。
4.  執行交換三部曲：
    *   讓 `prev.next` 指向 `second`。
    *   讓 `first.next` 指向 `second.next` (下一對的開頭)。
    *   讓 `second.next` 指向 `first`。
5.  將 `prev` 移動到 `first` 的位置，準備處理下一對。

## 3. 演算法設計 (Algorithm Design)

我們採用 **疊代法**。

**偽代碼 (Pseudo-code):**

```text
Function swapPairs(head):
    Initialize dummy = new ListNode(0, head)
    Initialize prev = dummy
    
    While prev.next is not None AND prev.next.next is not None:
        first = prev.next
        second = prev.next.next
        
        # 開始交換
        prev.next = second
        first.next = second.next
        second.next = first
        
        # 移動 prev 以處理下一對
        prev = first
        
    Return dummy.next
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   N 是節點總數。我們只遍歷了一次串列，每次移動兩個位置。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數來儲存指標。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import Optional

# 定義單向鏈結串列節點
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 建立一個啞節點指向 head，這可以簡化處理頭部交換的邏輯
        dummy = ListNode(0, head)
        # prev 指針指向「待交換的一對節點」的前一個節點
        prev = dummy
        
        # 2. 只要後面還有至少兩個節點，就進行交換
        while prev.next and prev.next.next:
            # 找出要交換的兩個節點
            # 假設目前是 prev -> 1 -> 2 -> 3
            first = prev.next       # 即節點 1
            second = prev.next.next # 即節點 2
            
            # 3. 開始執行交換邏輯
            
            # 第一步：讓 prev 指向 2
            # 結果變為: prev -> 2 , 1 -> 2 -> 3
            prev.next = second
            
            # 第二步：讓 1 指向 3 (下一對的起點)
            # 結果變為: prev -> 2 , 1 -> 3
            first.next = second.next
            
            # 第三步：讓 2 指向 1
            # 結果變為: prev -> 2 -> 1 -> 3
            second.next = first
            
            # 4. 移動 prev 指針，準備處理下一對
            # 注意：現在 1 已經變成這對中的後者了，所以 prev 應該移到 1
            prev = first
            
        # 最後返回啞節點的下一個，即新的頭節點
        return dummy.next
```
