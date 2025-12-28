# 0025 - Reverse Nodes in k-Group (K 個一組翻轉鏈結串列)

## 1. 題目理解 (Problem Comprehension)

給你一個鏈結串列，每 `k` 個節點一組進行翻轉，並返回修改後的鏈結串列。

**關鍵規則：**
1.  如果節點總數不是 `k` 的整數倍，那麼最後剩餘的節點應該保持原樣，不進行翻轉。
2.  你不能只是單純地改變節點內部的值，而是需要實際進行**節點指標 (Pointer)** 的翻轉。

這是一道 LeetCode 的 **Hard** 題目，它結合了「反轉鏈結串列」和「分組處理」的概念。

**輸入與輸出格式：**
*   **輸入 (Input):** `head`: 鏈結串列頭節點, `k`: 正整數。
*   **輸出 (Output):** 修改後的頭節點。

**範例：**
輸入: `1->2->3->4->5`, `k = 2`
輸出: `2->1->4->3->5`

## 2. 思路分析 (Thought Process)

這道題可以拆解成幾個重複的子問題：
1.  **分組**：找到每一組的開始和結束位置。
2.  **判斷長度**：如果當前剩餘的節點不足 `k` 個，停止翻轉。
3.  **翻轉小組**：對長度為 `k` 的小組進行翻轉。
4.  **連接**：將翻轉後的小組重新接回到原串列中。

**優化思路：疊代法 + 啞節點 (Iterative with Dummy Node)**
1.  使用 **啞節點 (Dummy Node)** 指向 `head`。
2.  維護一個 `group_prev` 指針，指向每一組的前一個節點。
3.  **尋找第 k 個節點**：從 `group_prev` 開始往後走 `k` 步。如果沒走到 `k` 步就遇到 `None`，代表剩下不足 `k` 個，任務結束。
4.  **保存下一組的起點**：記錄 `group_next = kth.next`。
5.  **翻轉當前組**：
    *   將該組內部的 `next` 指標反向。
    *   注意：原本該組的第一個節點，翻轉後要指向 `group_next`。
6.  **更新連接**：讓 `group_prev.next` 指向原本的第 `k` 個節點（現在的新組長）。
7.  **移動 `group_prev`**：移動到翻轉後的組末尾（即原本的組頭），準備處理下一組。

## 3. 演算法設計 (Algorithm Design)

我們採用 **分組疊代法**。

**偽代碼 (Pseudo-code):**

```text
Function reverseKGroup(head, k):
    Initialize dummy = new ListNode(0, head)
    group_prev = dummy
    
    While True:
        # 1. 找到第 k 個節點
        kth = getKth(group_prev, k)
        If kth is None: Break
        
        group_next = kth.next
        
        # 2. 翻轉這一組 (從 group_prev.next 到 kth)
        prev = kth.next
        curr = group_prev.next
        While curr != group_next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        # 3. 更新 group_prev 的指向，並移動到下一組的前面
        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp
        
    Return dummy.next
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   N 是節點總數。每個節點最多被訪問兩次（一次是找第 k 個，一次是翻轉）。
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. 建立啞節點指向 head
        dummy = ListNode(0, head)
        # group_prev 永遠指向每一組「待翻轉節點」的前一個位置
        group_prev = dummy
        
        while True:
            # 2. 找到當前組的第 k 個節點
            kth = self.get_kth(group_prev, k)
            if not kth:
                # 如果剩下的節點不足 k 個，直接跳出迴圈，不翻轉
                break
            
            # 記錄下一組的起點
            group_next = kth.next
            
            # 3. 翻轉當前這一組 (k 個節點)
            # 技巧：將 prev 設為 group_next，這樣翻轉後的組尾會自動接上下一組的開頭
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                # 標準的鏈結串列反轉邏輯
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # 4. 重新連接：將 group_prev 指向翻轉後的組頭 (即原本的第 k 個)
            # 原本的組頭現在變成了組尾，我們暫存它以便移動 group_prev
            new_group_end = group_prev.next
            group_prev.next = kth
            # 移動到下一組的前面
            group_prev = new_group_end
            
        return dummy.next
        
    def get_kth(self, curr, k):
        # 輔助函式：從 curr 開始往後找第 k 個節點
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
```
