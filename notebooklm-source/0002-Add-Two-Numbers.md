# 0002 - Add Two Numbers (兩數相加)

## 1. 題目理解 (Problem Comprehension)

給你兩個**非空 (non-empty)** 的鏈結串列 (Linked List)，它們分別代表兩個非負整數。
這些整數的位數是**逆序 (reverse order)** 儲存的，也就是說：鏈結串列的第一個節點代表「個位數」，第二個節點代表「十位數」，以此類推。
每個節點只儲存一個數字 (0-9)。

請你將這兩個數相加，並以相同的逆序鏈結串列形式返回結果。

**輸入與輸出格式：**

*   **輸入 (Input):**
    *   `l1`: 第一個鏈結串列的頭節點。
    *   `l2`: 第二個鏈結串列的頭節點。
*   **輸出 (Output):**
    *   一個新的鏈結串列的頭節點，代表相加後的結果。

**範例：**
`l1`: 2 -> 4 -> 3 (代表數字 342)
`l2`: 5 -> 6 -> 4 (代表數字 465)
相加：342 + 465 = 807
輸出: 7 -> 0 -> 8 (代表數字 807)

**限制條件：**
*   除了數字 0 本身，這兩個數字都不會以 0 開頭。

## 2. 思路分析 (Thought Process)

### 直觀模擬法

這題其實就是模擬我們小學時學的直式加法。
因為鏈結串列已經是「個位數」在最前面了，這跟我們做直式加法時從最右邊（個位）開始算的順序是一樣的，非常方便。

我們只需要同時遍歷兩個鏈結串列，將對應位置的數字相加，再加上前一位的「進位 (carry)」，就可以算出當前位數的結果。

*   **關鍵點：**
    1.  **對齊相加**: `l1` 的當前節點 + `l2` 的當前節點 + `carry`。
    2.  **進位處理**:
        *   新的 `carry` = 總和 // 10
        *   當前位數的值 = 總和 % 10
    3.  **長度不一**: 如果一個串列比另一個短，短的那個後面就當作是 0。
    4.  **最後進位**: 如果遍歷完所有節點後，`carry` 還是大於 0，記得要在最後補一個節點（例如 500 + 500 = 1000，最後會有一個進位 1）。

## 3. 演算法設計 (Algorithm Design)

我們使用一個 `while` 迴圈來遍歷 `l1` 和 `l2`。為了簡化程式碼，我們可以建立一個 `dummy_head` (啞節點) 來作為結果串列的開頭，這樣我們就不需要特別處理「第一個節點」的初始化邏輯。

**偽代碼 (Pseudo-code):**

```text
Function addTwoNumbers(l1, l2):
    Initialize dummy_head = new ListNode(0)
    Initialize curr = dummy_head
    Initialize carry = 0

    While l1 is not None OR l2 is not None OR carry != 0:
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0
        
        total = val1 + val2 + carry
        carry = total // 10  (Integer division)
        digit = total % 10   (Modulus)
        
        curr.next = new ListNode(digit)
        curr = curr.next
        
        if l1 is not None: l1 = l1.next
        if l2 is not None: l2 = l2.next

    Return dummy_head.next
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(max(N, M))**
    *   N 和 M 分別是兩個鏈結串列的長度。我們需要遍歷較長的那個串列一次。
*   **空間複雜度 (Space Complexity): O(max(N, M))**
    *   我們需要建立一個新的鏈結串列來儲存結果，其長度最多是 `max(N, M) + 1` (如果有最後進位)。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import Optional

# 定義單向鏈結串列節點
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 建立一個啞節點 (dummy head)，它的 next 將會指向真正的結果頭節點
        # 這樣做的好處是可以簡化處理頭節點的邏輯
        dummy_head = ListNode(0)
        curr = dummy_head  # curr 指標用來構建新的串列
        carry = 0          # 初始化進位為 0
        
        # 當 l1 或 l2 還有節點，或者還有進位 (carry) 沒處理完時，繼續迴圈
        while l1 or l2 or carry:
            # 如果 l1 還沒走完，取 l1 的值，否則當作 0
            val1 = l1.val if l1 else 0
            # 如果 l2 還沒走完，取 l2 的值，否則當作 0
            val2 = l2.val if l2 else 0
            
            # 計算當前位的總和：兩個數字加上前一位的進位
            total = val1 + val2 + carry
            
            # 計算新的進位 (例如 15 // 10 = 1)
            carry = total // 10
            # 計算當前位應該留下的數字 (例如 15 % 10 = 5)
            digit = total % 10
            
            # 建立一個新節點，並將它接到結果串列的後面
            curr.next = ListNode(digit)
            # 移動 curr 指標到最新的節點
            curr = curr.next
            
            # 如果 l1 還有節點，往下移動
            if l1: l1 = l1.next
            # 如果 l2 還有節點，往下移動
            if l2: l2 = l2.next
            
        # 返回啞節點的下一個節點，這才是真正的結果開頭
        return dummy_head.next
```
