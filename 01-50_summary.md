---
Source: notebooklm-source/0001-Two-Sum.md

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

---
Source: notebooklm-source/0002-Add-Two-Numbers.md

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

---
Source: notebooklm-source/0003-Longest-Substring-Without-Repeating-Characters.md

# 0003 - Longest Substring Without Repeating Characters (無重複字符的最長子串)

## 1. 題目理解 (Problem Comprehension)

給定一個字串 `s`，請找出其中**不包含重複字符**的**最長子串 (substring)** 的長度。

**輸入與輸出格式：**

*   **輸入 (Input):**
    *   `s`: 一個字串 (可能是空的，也可能包含空格、符號、數字等)。
*   **輸出 (Output):**
    *   一個整數 (int)，代表最長無重複字符子串的長度。

**範例：**
1.  `s = "abcabcbb"` -> 輸出 3 (因為 "abc" 是最長的無重複子串)
2.  `s = "bbbbb"` -> 輸出 1 (因為 "b" 是最長的)
3.  `s = "pwwkew"` -> 輸出 3 (因為 "wke" 是最長的，注意 "pwke" 有重複的 'w'，而且必須是**子串**，不能是子序列)

## 2. 思路分析 (Thought Process)

### 直觀解法：暴力法

最簡單的想法是檢查所有的子串，看看它們是否有重複字符。
*   兩層迴圈產生所有可能的子串 `s[i:j]`。
*   對每個子串檢查是否有重複字符 (可以用 Set)。
*   時間複雜度會達到 O(N^3)，因為子串有 O(N^2) 個，檢查重複又要 O(N)。這在字串很長時會超時。

### 優化思路：滑動窗口 (Sliding Window)

我們可以維護一個「窗口」，這個窗口內的字符保證是**沒有重複**的。
這個窗口由兩個指針定義：`left` (左邊界) 和 `right` (右邊界)。

1.  開始時，`left` 和 `right` 都指向開頭。
2.  我們移動 `right` 指針向右擴展窗口，將新的字符加入。
3.  如果新加入的字符**已經存在**於窗口中（重複了！），我們就需要移動 `left` 指針來縮小窗口，直到把那個重複的字符「移出」窗口為止。
4.  在每一步，我們都記錄當前窗口的大小 `right - left + 1`，並更新最大值。

**如何快速判斷字符是否在窗口中？**
我們可以用一個**雜湊表 (Hash Map)** 來記錄窗口內字符的位置，或者用一個 Set。如果是 Hash Map，我們可以記錄 `{字符: 索引}`。

**優化後的移動策略：**
當我們遇到重複字符 `char` 時，我們不需要一步一步移動 `left`。
如果我們知道上一次 `char` 出現的位置是 `prev_index`，那麼新的 `left` 至少要移動到 `prev_index + 1`，這樣才能避開重複。

## 3. 演算法設計 (Algorithm Design)

我們採用 **滑動窗口 + 雜湊表** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function lengthOfLongestSubstring(s):
    Initialize char_map = {} (Stores char -> index)
    Initialize left = 0
    Initialize max_len = 0

    For right from 0 to length(s) - 1:
        current_char = s[right]

        If current_char is in char_map AND char_map[current_char] >= left:
            # Found a duplicate inside the current window
            # Move left directly to the right of the previous occurrence
            left = char_map[current_char] + 1

        # Update the character's latest index
        char_map[current_char] = right
        
        # Calculate current window length and update max
        max_len = max(max_len, right - left + 1)

    Return max_len
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   我們只遍歷字串一次 (right 指針從頭走到尾)。
    *   left 指針也只會向右移動，不會回頭。
    *   Hash Map 的操作是 O(1)。
*   **空間複雜度 (Space Complexity): O(min(N, M))**
    *   我們需要存儲字符到 Hash Map。M 是字符集的大小（例如 ASCII 是 128，擴展 ASCII 是 256）。
    *   在最壞情況下，空間複雜度取決於字符集的大小，或者字串長度。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 用雜湊表記錄字符最後一次出現的索引
        # 格式: {字符: 索引}
        char_map = {}
        
        # 滑動窗口的左邊界
        left = 0
        
        # 記錄最長長度
        max_len = 0
        
        # right 指針向右遍歷字串
        for right, char in enumerate(s):
            # 如果當前字符已經在 map 中，並且它的位置在當前窗口內 (>= left)
            # 這表示出現了重複字符
            if char in char_map and char_map[char] >= left:
                # 將左邊界直接跳到重複字符的下一位
                # 這樣可以保證窗口內沒有重複的該字符
                left = char_map[char] + 1
            
            # 更新當前字符的索引為最新位置
            char_map[char] = right
            
            # 計算當前窗口長度 (right - left + 1)，並更新最大值
            max_len = max(max_len, right - left + 1)
            
        return max_len
```

---
Source: notebooklm-source/0004-Median-of-Two-Sorted-Arrays.md

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

---
Source: notebooklm-source/0005-Longest-Palindromic-Substring.md

# 0005 - Longest Palindromic Substring (最長迴文子串)

## 1. 題目理解 (Problem Comprehension)

給定一個字串 `s`，請找出其中最長的**迴文子串 (Palindromic Substring)**。
所謂「迴文」，就是正著讀和反著讀都一樣的字串，例如 "aba" 或 "abba"。

**輸入與輸出格式：**

*   **輸入 (Input):**
    *   `s`: 一個字串。
*   **輸出 (Output):**
    *   一個字串，即 `s` 中最長的那個迴文子串。如果有多個長度一樣的，返回其中一個即可。

**範例：**
1.  `s = "babad"` -> 輸出 "bab" 或 "aba"。
2.  `s = "cbbd"` -> 輸出 "bb"。

## 2. 思路分析 (Thought Process)

### 直觀解法：暴力法

最直觀的做法是：
1.  列出所有的子串 `s[i:j]`。
2.  檢查每一個子串是否為迴文。
3.  記錄長度最長的那個。

*   **複雜度分析：**
    *   子串有 O(N^2) 個。
    *   檢查一個子串是否為迴文需要 O(N) 時間。
    *   總時間複雜度 O(N^3)。這在 N 較大時會超時。

### 優化思路：中心擴展法 (Expand Around Center)

我們可以換個角度想：與其先找子串再檢查，不如先找「中心點」，然後往兩邊擴散，直到不是迴文為止。

**迴文的中心有兩種情況：**
1.  **奇數長度**：中心是一個字符，例如 "aba" 的中心是 'b'。
2.  **偶數長度**：中心是兩個字符之間，例如 "abba" 的中心是兩個 'b' 之間。

對於長度為 N 的字串：
*   有 N 個單字符中心。
*   有 N-1 個雙字符中心（相鄰兩個字符之間）。
*   總共有 2N - 1 個中心。

**策略：**
1.  遍歷這 2N - 1 個中心。
2.  對每個中心，同時向左和向右擴展 (`left--`, `right++`)，只要 `s[left] == s[right]` 就繼續。
3.  記錄下每個中心能擴展到的最大長度，並更新全局最大值。

## 3. 演算法設計 (Algorithm Design)

我們採用 **中心擴展法**。

**偽代碼 (Pseudo-code):**

```text
Function longestPalindrome(s):
    If s is empty, return ""
    Initialize start = 0, end = 0

    For i from 0 to length(s) - 1:
        # 情況 1: 奇數長度，以 s[i] 為中心
        len1 = expandAroundCenter(s, i, i)
        
        # 情況 2: 偶數長度，以 s[i] 和 s[i+1] 為中心
        len2 = expandAroundCenter(s, i, i + 1)
        
        len = max(len1, len2)
        
        If len > end - start:
            # 更新最長迴文的起始和結束位置
            start = i - (len - 1) / 2
            end = i + len / 2

    Return s[start : end + 1]

Function expandAroundCenter(s, left, right):
    While left >= 0 AND right < length(s) AND s[left] == s[right]:
        left--
        right++
    Return right - left - 1  (因為最後一次迴圈多減了一次 left，多加了一次 right)
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N^2)**
    *   我們遍歷了 2N-1 個中心。
    *   每個中心最多向兩邊擴展 N/2 次。
    *   雖然總體還是 O(N^2)，但實際上比暴力法快很多，因為大多數中心的擴展次數很少。而且空間複雜度低，不需額外空間。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只需要幾個變數來存儲索引，不需要額外的資料結構（如動態規劃表）。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 如果字串為空，直接返回空字串
        if not s:
            return ""
        
        # 記錄最長迴文子串的起始和結束索引
        start, end = 0, 0
        
        # 遍歷每一個可能的中心點
        for i in range(len(s)):
            # 情況 1: 以 s[i] 為中心 (奇數長度迴文)
            len1 = self.expandAroundCenter(s, i, i)
            # 情況 2: 以 s[i] 和 s[i+1] 為中心 (偶數長度迴文)
            len2 = self.expandAroundCenter(s, i, i + 1)
            
            # 取兩者中較長的那個
            max_len = max(len1, len2)
            
            # 如果找到比目前記錄還長的迴文，更新 start 和 end
            # 注意這裡的索引計算要小心：
            # 如果 max_len 是奇數 (例如 3)，i 是中心。start = i - 1 = i - 2//2
            # 如果 max_len 是偶數 (例如 2)，i 是左邊那個中心。start = i - 0 = i - 1//2
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        # 返回找到的最長迴文子串
        return s[start:end+1]
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        # 當左右指針在範圍內，且字符相等時，繼續往兩邊擴展
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # 回圈結束時，left 和 right 已經是不符合條件的位置了
        # 例如如果是 "aba"，最後 left=-1, right=3
        # 長度 = right - left - 1 = 3 - (-1) - 1 = 3
        return right - left - 1
```

---
Source: notebooklm-source/0006-ZigZag-Conversion.md

# 0006 - ZigZag Conversion (Z 字形變換)

## 1. 題目理解 (Problem Comprehension)

將一個給定的字串 `s` 根據指定的行數 `numRows`，以從上到下、從左到右的 Z 字形進行排列。

例如，字串為 `"PAYPALISHIRING"`，行數為 `3` 時，排列如下：
```text
P   A   H   N
A P L S I I G
Y   I   R
```
之後，我們按行讀取字符：`"PAHNAPLSIIGYIR"`。

**輸入與輸出格式：**
*   **輸入 (Input):**
    *   `s`: 一個字串。
    *   `numRows`: 一個整數，代表行數。
*   **輸出 (Output):**
    *   變換後的字串。

## 2. 思路分析 (Thought Process)

### 直觀解法：模擬排列過程

我們不需要真的去畫出一個二維矩陣（那樣會浪費很多空間）。我們只需要知道每個字符應該屬於哪一行，然後最後按順序把每一行的字符拼接起來即可。

想像一個電梯在 `numRows` 層樓之間上下移動：
1.  從第 0 行開始，往下走 (0, 1, 2, ...)。
2.  到達第 `numRows - 1` 行後，往回走 (... 2, 1, 0)。
3.  到達第 0 行後，再次往下走。

**核心邏輯：**
*   我們用一個列表 `rows` 來儲存每一行的內容，`rows[i]` 是一個字串，代表第 `i` 行目前收集到的字符。
*   我們用一個變數 `index` 追蹤目前在哪一行。
*   我們用一個變數 `step` 來控制方向：向下走時 `step = 1`，向上走時 `step = -1`。
*   當 `index` 到達 0 或 `numRows - 1` 時，我們就反轉 `step` 的正負號。

## 3. 演算法設計 (Algorithm Design)

我們採用 **模擬與方向控制** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function convert(s, numRows):
    If numRows == 1 or numRows >= length(s):
        Return s

    Initialize rows = array of empty strings, size numRows
    Initialize index = 0
    Initialize step = 1

    For each char in s:
        Append char to rows[index]
        
        If index == 0:
            step = 1
        Else if index == numRows - 1:
            step = -1
        
        index = index + step

    Return join(rows)
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   我們只需要遍歷一次字串 `s`，其中 N 是字串的長度。
*   **空間複雜度 (Space Complexity): O(N)**
    *   我們使用了 `rows` 列表來儲存字符，最終總長度還是 N。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 如果只有一行，或者行數比字串還長，不需要變換，直接返回
        if numRows == 1 or numRows >= len(s):
            return s
        
        # 建立一個列表，用來存放每一行的字符
        rows = [''] * numRows
        
        # index 代表目前在哪一行，step 代表移動的方向 (1 是向下，-1 是向上)
        index, step = 0, 1
        
        for char in s:
            # 將當前字符加入對應的行
            rows[index] += char
            
            # 如果走到了第一行，接下來要往下走 (step = 1)
            if index == 0:
                step = 1
            # 如果走到了最後一行，接下來要往上走 (step = -1)
            elif index == numRows - 1:
                step = -1
            
            # 根據方向移動到下一行
            index += step
            
        # 最後將所有行的字串拼接起來即為答案
        return ''.join(rows)
```

---
Source: notebooklm-source/0007-Reverse-Integer.md

# 0007 - Reverse Integer (整數反轉)

## 1. 題目理解 (Problem Comprehension)

給你一個 32 位元的有號整數 `x`，請你將這個整數中每一位數字進行反轉。

**特別注意：**
如果反轉後的整數超過了 32 位元有號整數的範圍 `[-2^31, 2^31 - 1]`，則返回 0。

**輸入與輸出格式：**
*   **輸入 (Input):** `x` (int)
*   **輸出 (Output):** 反轉後的整數 (int)，若溢位則為 0。

**範例：**
*   `123` -> `321`
*   `-123` -> `-321`
*   `120` -> `21`

## 2. 思路分析 (Thought Process)

### 如何反轉數字？

我們可以用數學的方法，不斷地取「個位數」並將它加到新數字的末尾。

1.  準備一個 `res = 0`。
2.  取出 `x` 的個位數：`pop = x % 10`。
3.  將 `res` 往左移一位並加上 `pop`：`res = res * 10 + pop`。
4.  將 `x` 去掉個位數：`x = x // 10`。
5.  重複上述步驟直到 `x` 變為 0。

### 處理負數與溢位

*   **負數**：在 Python 中，對負數取餘數 (`%`) 和地板除法 (`//`) 的行為可能與其他語言（如 C++ 或 Java）不同。為了簡單起見，我們可以先處理 `x` 的絕對值，記錄符號，最後再乘回去。
*   **溢位**：題目明確要求我們考慮 32 位元限制。反轉完成後，檢查結果是否落在 `[-2147483648, 2147483647]` 之間。

## 3. 演算法設計 (Algorithm Design)

我們採用 **數學取餘法**。

**偽代碼 (Pseudo-code):**

```text
Function reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    res = 0
    
    While x > 0:
        digit = x % 10
        res = res * 10 + digit
        x = x // 10
        
    res = res * sign
    
    If res < -2^31 or res > 2^31 - 1:
        Return 0
        
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(log10(x))**
    *   數字 `x` 大約有 `log10(x)` 位數字，我們迴圈的次數等於位數。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def reverse(self, x: int) -> int:
        # 記錄符號，並將 x 轉為正數處理，避免 Python 負數取餘數的特殊行為
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        
        # 當 x 還大於 0 時，繼續取出最後一位數字
        while x != 0:
            # 取出最後一位數字 (個位)
            digit = x % 10
            # 將目前結果乘以 10 (左移一位)，再加上取出的數字
            res = res * 10 + digit
            # 去掉 x 的最後一位數字
            x //= 10
            
        # 將原本的符號補回來
        res *= sign
        
        # 檢查是否超出 32 位元有號整數範圍 [-2^31, 2^31 - 1]
        # -2^31 = -2147483648
        # 2^31 - 1 = 2147483647
        if res < -2**31 or res > 2**31 - 1:
            return 0
            
        return res
```

---
Source: notebooklm-source/0008-String-to-Integer-atoi.md

# 0008 - String to Integer (atoi) (字串轉換整數)

## 1. 題目理解 (Problem Comprehension)

這道題目要求我們實現一個類似 C 語言中的 `atoi` 函式，將一個字串轉換成一個 32 位元的有號整數。

**轉換規則：**
1.  **忽略前導空格**：跳過字串開頭的所有空白字符。
2.  **判斷符號**：檢查第一個非空格字符是否為 `'+'` 或 `'-'`，這決定了最終結果的正負。如果都沒有，預設為正。
3.  **讀取數字**：讀取接下來的所有數字字符，直到遇到第一個非數字字符或字串結束。忽略後面的所有內容。
4.  **範圍限制**：如果轉換後的數字超出了 32 位元有號整數的範圍 `[-2^31, 2^31 - 1]`，則將其限制（Clamp）在邊界值。
5.  **無效情況**：如果第一個非空格字符不是符號或數字，或者字串只有空格，則返回 0。

## 2. 思路分析 (Thought Process)

這是一道典型的「字串處理」與「邊界處理」題目。我們需要按照題目要求的順序，一步一步進行檢查。

**步驟分解：**
1.  **清理空白**：使用 `strip()` 或手動移動索引跳過空格。
2.  **處理正負號**：檢查第一個字符，如果是 `'+'` 或 `'-'`，記錄符號並將索引往後移。
3.  **逐位轉換數字**：
    *   遍歷剩下的字符。
    *   如果是數字，將其轉換為整數並累加：`res = res * 10 + int(char)`。
    *   如果不是數字，立即停止。
4.  **處理邊界 (Clamp)**：
    *   Python 的整數不會溢位，所以我們可以先算出完整結果，最後再檢查是否超出 `[-2^31, 2^31 - 1]`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **線性遍歷與規則檢查**。

**偽代碼 (Pseudo-code):**

```text
Function myAtoi(s):
    1. s = trim whitespace from start of s
    2. If s is empty, return 0
    
    3. Initialize sign = 1, index = 0
    4. If s[0] == '+':
           index++
       Else if s[0] == '-':
           sign = -1
           index++
    
    5. Initialize res = 0
    6. While index < length(s) and s[index] is a digit:
           res = res * 10 + digit(s[index])
           index++
    
    7. res = res * sign
    
    8. Clamp res to [-2^31, 2^31 - 1]
    
    9. Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   我們最多只需要遍歷字串一次。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只需要幾個變數來存儲結果、符號和索引。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. 移除字串開頭和結尾的空白字符
        s = s.strip()
        
        # 2. 如果清理後字串為空，直接返回 0
        if not s:
            return 0
        
        sign = 1  # 預設符號為正
        i = 0     # 當前處理字串的索引
        
        # 3. 處理符號部分
        if s[i] == '+':
            # 遇到正號，索引往後移，符號不變
            i += 1
        elif s[i] == '-':
            # 遇到負號，索引往後移，符號設為 -1
            sign = -1
            i += 1
            
        res = 0
        # 4. 遍歷字串，直到遇到非數字字符或結束
        while i < len(s) and s[i].isdigit():
            # 將目前的數字加到結果中
            # int(s[i]) 將字符 '5' 轉為整數 5
            res = res * 10 + int(s[i])
            i += 1
            
        # 5. 加上符號
        res *= sign
        
        # 6. 處理 32 位元溢位限制 (Clamping)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res
```

---
Source: notebooklm-source/0009-Palindrome-Number.md

# 0009 - Palindrome Number (迴文數)

## 1. 題目理解 (Problem Comprehension)

給你一個整數 `x`，如果 `x` 是一個迴文整數，返回 `true`；否則，返回 `false`。

迴文數是指正序（從左向右）和倒序（從右向左）讀都是一樣的整數。

**輸入與輸出格式：**
*   **輸入 (Input):** `x` (int)
*   **輸出 (Output):** `True` 或 `False` (bool)

**範例：**
*   `121` -> `True`
*   `-121` -> `False` (從右向左讀為 `121-`，不相等)
*   `10` -> `False` (從右向左讀為 `01`)

**進階挑戰：**
你能不將整數轉為字串來解決這個問題嗎？

## 2. 思路分析 (Thought Process)

### 直觀解法：轉為字串

最簡單的方法是把數字轉成字串，然後檢查字串是否跟反轉後的自己相等。
但在面試中，面試官通常希望你用數學方法解決，不使用字串轉換。

### 優化思路：反轉一半數字

我們可以參考「反轉整數」的做法，但為了避免反轉後數字太大造成溢位（雖然 Python 不會溢位，但在其他語言會），我們只需要**反轉一半**的數字。

**核心邏輯：**
1.  **排除明顯不符合的情況**：
    *   負數一定不是迴文。
    *   如果數字最後一位是 0，除非該數字就是 0，否則一定不是迴文（因為開頭不會是 0）。
2.  **反轉後一半**：
    *   將數字 `x` 的後半段反轉成 `reversed_half`。
    *   如何知道已經反轉到一半了？當 `x` 變得小於或等於 `reversed_half` 時。
3.  **比較**：
    *   如果數字位數是偶數（如 1221），則 `x == reversed_half` (12 == 12)。
    *   如果數字位數是奇數（如 121），最後會變成 `x = 1`, `reversed_half = 12`。此時中間的數字不影響迴文，所以我們比較 `x == reversed_half // 10` (1 == 1)。

## 3. 演算法設計 (Algorithm Design)

我們採用 **反轉一半數字** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function isPalindrome(x):
    # 排除特殊情況
    If x < 0 OR (x % 10 == 0 AND x != 0):
        Return False
    
    Initialize reversed_half = 0
    While x > reversed_half:
        # 取出 x 的最後一位並加入 reversed_half
        reversed_half = reversed_half * 10 + (x % 10)
        x = x // 10
        
    # 當長度為奇數時，藉由 reversed_half // 10 去掉中間位數
    Return x == reversed_half OR x == reversed_half // 10
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(log10(x))**
    *   我們只處理了數字的一半位數，所以時間是 O(log10(x) / 2)，簡化為 O(log10(x))。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只需要常數個變數儲存反轉後的數字。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 排除所有負數，以及最後一位是 0 的正整數（因為第一位不可能為 0，除非是 0 本身）
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        # 將數字 x 的後半段取出並反轉
        # 當 x <= reversed_half 時，表示我們已經處理到中間位置了
        while x > reversed_half:
            # 取出 x 的個位數
            last_digit = x % 10
            # 將這個數字加到反轉變數中
            reversed_half = reversed_half * 10 + last_digit
            # 將 x 的最後一位移除
            x //= 10
            
        # 如果數字是偶數位數（例如 1221），最後 x=12, reversed_half=12
        # 如果數字是奇數位數（例如 121），最後 x=1, reversed_half=12
        # 在奇數情況下，中間的數字 2 被存在 reversed_half 的個位，
        # 我們可以用 reversed_half // 10 把這個中間位去掉，再跟 x 比較
        return x == reversed_half or x == reversed_half // 10
```
---
Source: notebooklm-source/0010-Regular-Expression-Matching.md

# 0010 - Regular Expression Matching (正則表達式匹配)

## 1. 題目理解 (Problem Comprehension)

這是一道 LeetCode 的 **Hard** 題目。你需要實現一個簡化版的正則表達式匹配：

*   `.`：匹配任意**單個**字符。
*   `*`：匹配**零個或多個**前面的那個元素。
*   匹配必須覆蓋**整個**輸入字串 `s`。

**輸入與輸出格式：**
*   **輸入 (Input):**
    *   `s`: 待匹配的字串。
    *   `p`: 正則表達式模式。
*   **輸出 (Output):** `True` 或 `False`。

**範例：**
1.  `s = "aa", p = "a"` -> `False`
2.  `s = "aa", p = "a*"` -> `True` ('*' 匹配了兩次 'a')
3.  `s = "ab", p = ".*"` -> `True` ('.' 匹配了 'a', '*' 讓它重複匹配了 'b')

## 2. 思路分析 (Thought Process)

這題最難的地方在於 `*` 的處理。當我們遇到 `x*` 時，它可以匹配 0 個 `x`、1 個 `x`、2 個 `x` 等等。這會導致很多種分支，因此非常適合用**動態規劃 (Dynamic Programming, DP)** 來解決。

### 狀態定義
我們定義 `dp[i][j]` 表示「字串 `s` 從索引 `i` 開始的子串」是否能被「模式 `p` 從索引 `j` 開始的子串」所匹配。

### 轉移方程
1.  **首字符匹配判斷**：
    `first_match = (i < len(s)) and (p[j] == s[i] or p[j] == '.')`

2.  **處理 `*` (即檢查 `p[j+1]` 是否為 `*`)**：
    *   **情況 A：匹配 0 次**。我們直接跳過 `p[j]` 和 `p[j+1]`。
        `dp[i][j] = dp[i][j+2]`
    *   **情況 B：匹配 1 次或多次**。前提是 `first_match` 為真，然後我們繼續用同一個模式去匹配 `s` 的下一個位置。
        `dp[i][j] = first_match and dp[i+1][j]`
    *   **兩者取其一**：`dp[i][j] = (情況 A) or (情況 B)`

3.  **一般情況 (沒有 `*`)**：
    *   只要 `first_match` 為真，並且剩下的部分也匹配。
        `dp[i][j] = first_match and dp[i+1][j+1]`

### 基礎情況 (Base Case)
*   當 `i` 和 `j` 都到達末尾時，`dp[len(s)][len(p)] = True`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **自底向上 (Bottom-up) 的動態規劃**。

**偽代碼 (Pseudo-code):**

```text
Function isMatch(s, p):
    Initialize dp table [len(s)+1][len(p)+1] with False
    dp[len(s)][len(p)] = True

    For i from len(s) down to 0:
        For j from len(p)-1 down to 0:
            first_match = (i < len(s) and (p[j] == s[i] or p[j] == '.'))
            
            If j + 1 < len(p) and p[j+1] == '*':
                # Case 1: 0 occurrences, Case 2: 1+ occurrences
                dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
            Else:
                # Normal match
                dp[i][j] = first_match and dp[i+1][j+1]

    Return dp[0][0]
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(S * P)**
    *   S 和 P 分別是字串和模式的長度。我們需要填滿一個 S*P 的矩陣。
*   **空間複雜度 (Space Complexity): O(S * P)**
    *   需要一個二維陣列來儲存 DP 狀態。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] 代表 s[i:] 是否與 p[j:] 匹配
        # 我們多開一列和一行來處理空字串的情況
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # 空字串與空模式當然匹配
        dp[len(s)][len(p)] = True
        
        # 從後往前填表
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                # 檢查當前第一個字符是否匹配
                # 注意 i < len(s) 是為了防止 s 已經用完但 p 還沒完的情況
                first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
                
                # 如果下一個字符是 '*'
                if j + 1 < len(p) and p[j+1] == '*':
                    # '*' 的兩種選法：
                    # 1. 匹配 0 個：忽略目前的字符和 '*'，看 p[j+2:] 的結果
                    # 2. 匹配 1 個以上：目前首字必須匹配，然後看 s[i+1:] 是否能被目前的 p[j:] 匹配
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    # 沒有 '*'，就是單純的匹配首字，並遞迴看剩下的
                    dp[i][j] = first_match and dp[i+1][j+1]
                    
        # 最終答案在 dp[0][0]
        return dp[0][0]
```

---
Source: notebooklm-source/0011-Container-With-Most-Water.md

# 0011 - Container With Most Water (盛最多水的容器)

## 1. 題目理解 (Problem Comprehension)

給定一個長度為 `n` 的整數陣列 `height`。有 `n` 條垂線，第 `i` 條線的兩個端點分別為 `(i, 0)` 和 `(i, height[i])`。

找出其中的兩條線，使得它們與 x 軸共同構成的容器可以容納最多的水。返回容器可以儲存的最大水量。

**輸入與輸出格式：**
*   **輸入 (Input):** `height`: 一個整數列表。
*   **輸出 (Output):** `max_area`: 最大水容量（整數）。

**限制：**
*   你不能傾斜容器。
*   容量 = 底 (兩個索引之差) * 高 (兩條線中較短的那條)。

## 2. 思路分析 (Thought Process)

### 直觀解法：暴力法

檢查每一對可能的垂直線組合 `(i, j)`，計算它們能盛的水量，然後取最大值。
*   迴圈 `i` 從 0 到 `n-1`，迴圈 `j` 從 `i+1` 到 `n-1`。
*   `area = (j - i) * min(height[i], height[j])`。
*   時間複雜度：O(N^2)。當 N 很大時會超時。

### 優化思路：雙指針 (Two Pointers)

我們可以用兩個指針 `left` 和 `right` 分別指向陣列的兩端。

**為什麼這樣做有效？**
容器的容量由兩個因素決定：**寬度 (Width)** 和 **高度 (Height)**。
*   當指針在兩端時，我們擁有最大的「寬度」。
*   當我們移動指針時，「寬度」一定會變小。
*   為了補償變小的寬度，我們必須尋求更大的「高度」。
*   高度是由兩邊較短的那條線決定的。因此，如果我們移動較長的那條線，高度只會變小或不變（因為短的那條沒變），寬度又變小了，面積一定變小。
*   **結論**：我們應該移動**較短**的那條線，看看能不能換到一條更長的線來增加高度。

## 3. 演算法設計 (Algorithm Design)

我們採用 **雙指針** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function maxArea(height):
    Initialize left = 0, right = length(height) - 1
    Initialize max_area = 0

    While left < right:
        # 計算當前面積
        current_width = right - left
        current_height = min(height[left], height[right])
        current_area = current_width * current_height
        
        # 更新最大面積
        max_area = max(max_area, current_area)
        
        # 移動較短的那一邊
        If height[left] < height[right]:
            left++
        Else:
            right--

    Return max_area
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   我們只遍歷了陣列一次。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 初始化左右指針分別指向陣列的首尾
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # 容器的寬度是兩個指針之間的距離
            width = right - left
            # 容器的高度取決於左右兩條線中較短的那一條 (木桶效應)
            h = min(height[left], height[right])
            
            # 計算當前面積並更新最大值
            current_area = width * h
            if current_area > max_area:
                max_area = current_area
            
            # 核心邏輯：移動較短的那一側指針
            # 因為寬度已經在變小了，只有移動短的那邊才有機會讓高度增加，進而增加面積
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
```
---
Source: notebooklm-source/0012-Integer-to-Roman.md

# 0012 - Integer to Roman (整數轉羅馬數字)

## 1. 題目理解 (Problem Comprehension)

羅馬數字包含以下七種字符：`I`, `V`, `X`, `L`, `C`, `D` 和 `M`。

| 字符 | 數值 |
| :--- | :--- |
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

**規則：**
1.  一般情況下，較大的數字在左邊，相加得到結果（如 `XII` = 12）。
2.  **特例（減法）：**
    *   `I` 在 `V`(5) 或 `X`(10) 之前，表示 4 或 9。
    *   `X` 在 `L`(50) 或 `C`(100) 之前，表示 40 或 90。
    *   `C` 在 `D`(500) 或 `M`(1000) 之前，表示 400 或 900。

給你一個 1 到 3999 之間的整數，請將其轉換為羅馬數字。

## 2. 思路分析 (Thought Process)

這道題可以看作是一個「找零錢」的問題。我們有一堆不同面值的羅馬數字（包含特例），我們想用盡可能大的面值去組合出目標數字。

**策略：**
1.  將所有基本的羅馬數字和 6 個特例按**從大到小**列出來。
2.  從最大的面值 (1000, 'M') 開始，看目前的 `num` 裡面包含幾個這個面值。
3.  將對應數量的符號加入結果字串，並從 `num` 中減去對應的數值。
4.  移向下一種面值，重複直到 `num` 變為 0。

## 3. 演算法設計 (Algorithm Design)

我們採用 **貪心演算法 (Greedy Algorithm)**。

**偽代碼 (Pseudo-code):**

```text
Function intToRoman(num):
    Define pairs = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    
    Initialize result = ""
    
    For value, symbol in pairs:
        While num >= value:
            num = num - value
            result = result + symbol
            
    Return result
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(1)**
    *   雖然看起來有個迴圈，但由於 `num` 的最大值被限制在 3999，且羅馬數字的符號數量是固定的常數。
*   **空間複雜度 (Space Complexity): O(1)**
    *   儲存對應關係的空間是固定的。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        # 建立一個清單，包含所有的羅馬數字基礎值和特殊減法情況
        # 順序必須從大到小，這樣我們才能實施「貪心」策略
        value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        
        res = []
        
        # 遍歷所有的面值
        for value, symbol in value_map:
            # 如果剩餘的數字已經是 0，可以提早結束
            if num == 0:
                break
            
            # 使用 divmod 同時取得商數 (count) 和餘數 (num)
            # count 代表 num 裡面可以塞進幾個當前面值
            count, num = divmod(num, value)
            
            # 將該符號重複對應次數並加入結果清單
            # Python 中字串乘以數字可以重複字串，例如 'M' * 3 = 'MMM'
            res.append(symbol * count)
            
        # 最後將所有字串片段拼接起來
        return "".join(res)
```
---
Source: notebooklm-source/0013-Roman-to-Integer.md

# 0013 - Roman to Integer (羅馬數字轉整數)

## 1. 題目理解 (Problem Comprehension)

羅馬數字包含以下七種字符：`I`, `V`, `X`, `L`, `C`, `D` 和 `M`。

| 字符 | 數值 |
| :--- | :--- |
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

**規則：**
1.  通常大的數字在左，小的在右，直接相加。
2.  **特例（減法）：** 當較小的符號位在較大的符號左側時，需要減去較小的數值。
    *   `IV` = 5 - 1 = 4
    *   `IX` = 10 - 1 = 9
    *   `XL` = 50 - 10 = 40
    *   `XC` = 100 - 10 = 90
    *   `CD` = 500 - 100 = 400
    *   `CM` = 1000 - 100 = 900

給你一個羅馬數字字串，請將其轉換為整數。

## 2. 思路分析 (Thought Process)

我們只需要遍歷字串，將每個字符對應的數值加起來即可。唯一的挑戰是如何處理那 6 個「減法」特例。

**規律觀察：**
*   在 `III` (3) 中，`I` 後面還是 `I`，相等，所以 `1 + 1 + 1`。
*   在 `IV` (4) 中，`I`(1) 後面是 `V`(5)，**1 小於 5**，所以這是一個減法情況，結果是 `-1 + 5 = 4`。
*   在 `VI` (6) 中，`V`(5) 後面是 `I`(1)，**5 大於 1**，所以是正常的加法，結果是 `5 + 1 = 6`。

**結論：**
對於位置 `i` 的字符，我們看它右邊的字符（位置 `i+1`）：
1.  如果 `value(s[i]) < value(s[i+1])`，則結果要**減去** `value(s[i])`。
2.  否則，結果**加上** `value(s[i])`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **單次遍歷與前瞻比較**。

**偽代碼 (Pseudo-code):**

```text
Function romanToInt(s):
    Initialize map = {'I': 1, 'V': 5, ...}
    Initialize total = 0
    
    For i from 0 to length(s) - 1:
        current_val = map[s[i]]
        
        If i + 1 < length(s) AND current_val < map[s[i+1]]:
            total = total - current_val
        Else:
            total = total + current_val
            
    Return total
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   我們只需要遍歷一次字串 `s`。
*   **空間複雜度 (Space Complexity): O(1)**
    *   雜湊表的大小是固定的（7 個字符），與輸入規模無關。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        # 定義羅馬數字對應的數值對照表
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # 遍歷字串中的每一個字符
        for i in range(n):
            current_val = roman_map[s[i]]
            
            # 關鍵判斷：
            # 如果目前字符的數值小於「下一個」字符的數值，
            # 根據羅馬數字規則，這是一個減法特例（如 IV, IX, XL 等）
            if i + 1 < n and current_val < roman_map[s[i + 1]]:
                # 此時應該減去當前的數值
                total -= current_val
            else:
                # 否則，這是一個正常的加法
                total += current_val
                
        return total
```
---
Source: notebooklm-source/0014-Longest-Common-Prefix.md

# 0014 - Longest Common Prefix (最長公共前綴)

## 1. 題目理解 (Problem Comprehension)

編寫一個函式來查找字串陣列中的最長公共前綴。
如果不存在公共前綴，返回空字串 `""`。

**輸入與輸出格式：**
*   **輸入 (Input):** `strs`: 一個字串列表 (List[str])。
*   **輸出 (Output):** 最長公共前綴 (str)。

**範例：**
1.  `["flower","flow","flight"]` -> `"fl"`
2.  `["dog","racecar","car"]` -> `""`

## 2. 思路分析 (Thought Process)

這道題有多種解法，最常見的有：

### 方法一：水平掃描 (Horizontal Scanning)
先拿前兩個字串找公共前綴 LCP，再拿 LCP 去跟第三個字串找公共前綴，以此類推。
*   `LCP(S1, S2, S3) = LCP(LCP(S1, S2), S3)`

### 方法二：垂直掃描 (Vertical Scanning) - **推薦**
我們一列一列地比較字符。
*   先看所有字串的第 0 個字符是否相同？相同就繼續。
*   再看所有字串的第 1 個字符是否相同？
*   一旦發現某個字串比較短（走到底了），或者某個字符不同，就立即停止。

**優點：** 如果最短的那個公共前綴非常短（甚至沒有），垂直掃描可以非常快地結束。

## 3. 演算法設計 (Algorithm Design)

我們採用 **垂直掃描** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function longestCommonPrefix(strs):
    If strs is empty, return ""
    
    For i from 0 to length(strs[0]) - 1:
        char = strs[0][i]
        
        For j from 1 to length(strs) - 1:
            # 檢查第 j 個字串是否已經走完，或者字符不匹配
            If i == length(strs[j]) OR strs[j][i] != char:
                # 返回目前的公共前綴
                Return strs[0] 從 0 到 i-1 的子串
                
    Return strs[0]
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(S)**
    *   S 是所有字串中字符的總數。在最壞的情況下（所有字串都一樣），我們需要比較每個字符。
*   **空間複雜度 (Space Complexity): O(1)**
    *   我們只使用了少數幾個索引變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 如果輸入列表為空，返回空字串
        if not strs:
            return ""
        
        # 採用垂直掃描：以第一個字串為基準，逐位比較
        # i 代表目前比較到第幾個字符
        for i in range(len(strs[0])):
            # 取出第一個字串的第 i 個字符
            char = strs[0][i]
            
            # 將這個字符與剩下的所有字串進行比較
            for j in range(1, len(strs)):
                # 如果目前的索引 i 已經超過了第 j 個字串的長度
                # 或者第 j 個字串在第 i 位與基準字符不匹配
                if i == len(strs[j]) or strs[j][i] != char:
                    # 說明公共前綴到此為止，返回之前匹配好的部分
                    return strs[0][:i]
                    
        # 如果整個迴圈跑完都沒有中斷，說明第一個字串本身就是所有人的公共前綴
        return strs[0]
```
---
Source: notebooklm-source/0015-3Sum.md

# 0015 - 3Sum (三數之和)

## 1. 題目理解 (Problem Comprehension)

給你一個包含 `n` 個整數的陣列 `nums`，判斷 `nums` 中是否存在三個元素 `a, b, c`，使得 `a + b + c = 0`？

請找出所有和為 0 且**不重複**的三元組。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 整數列表。
*   **輸出 (Output):** 所有不重複的三元組列表 (List[List[int]])。

**限制：**
*   答案中不可以包含重複的三元組。

**範例：**
`nums = [-1, 0, 1, 2, -1, -4]`
輸出: `[[-1, -1, 2], [-1, 0, 1]]`

## 2. 思路分析 (Thought Process)

### 直觀解法：暴力法
使用三層迴圈遍歷所有組合，然後用一個 Set 來去除重複。
*   時間複雜度：O(N^3)。
*   空間複雜度：O(N) 用於儲存結果。
這在面試中通常是不可接受的，因為 N 如果是 3000，N^3 會達到 270 億，遠超運算限制。

### 優化思路：排序 + 雙指針 (Sorting + Two Pointers)
如果我們能把三數之和簡化為「兩數之和」，問題就會變簡單。

1.  **排序**：先將 `nums` 從小到大排序。排序是處理「重複」的關鍵。
2.  **固定一個數**：遍歷陣列，假設目前的數是 `nums[i]`。
3.  **尋找另外兩個數**：在 `nums[i]` 之後的區間 `[i+1, n-1]` 中，使用雙指針 `left` 和 `right` 尋找兩個數，使得 `nums[left] + nums[right] = -nums[i]`。
    *   如果和太小，`left` 右移。
    *   如果和太大，`right` 左移。
    *   如果正好相等，記錄答案，並跳過所有重複的 `nums[left]` 和 `nums[right]`。

**如何避免重複？**
*   當固定 `nums[i]` 時，如果 `nums[i] == nums[i-1]`，則直接跳過這次迴圈。
*   當找到一組解後，移動 `left` 和 `right` 時，也要跳過相同的數字。

## 3. 演算法設計 (Algorithm Design)

我們採用 **排序 + 雙指針** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function threeSum(nums):
    Sort nums
    Initialize res = []
    n = length(nums)

    For i from 0 to n - 3:
        # 避免重複
        If i > 0 AND nums[i] == nums[i-1]:
            Continue
        
        # 雙指針尋找剩下兩數
        left = i + 1
        right = n - 1
        While left < right:
            total = nums[i] + nums[left] + nums[right]
            If total == 0:
                Add [nums[i], nums[left], nums[right]] to res
                # 再次避免重複
                While left < right AND nums[left] == nums[left+1]: left++
                While left < right AND nums[right] == nums[right-1]: right--
                left++
                right--
            Else if total < 0:
                left++
            Else:
                right--

    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N^2)**
    *   排序需要 O(N log N)。
    *   外部迴圈跑 N 次，內部雙指針跑 N 次，總共 O(N^2)。
*   **空間複雜度 (Space Complexity): O(log N)** 到 **O(N)**
    *   取決於排序演算法所需的空間。在 Python 中通常是 O(N)。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. 首先對陣列進行排序，這是使用雙指針的前提
        nums.sort()
        res = []
        n = len(nums)
        
        # 2. 遍歷陣列，固定第一個數字 nums[i]
        # 我們只需要遍歷到倒數第三個，因為後面要留兩個位置給 left 和 right
        for i in range(n - 2):
            # 如果目前數字大於 0，因為後面的數字只會更大，
            # 所以三數之和不可能等於 0，可以直接結束
            if nums[i] > 0:
                break
            
            # 關鍵：跳過重複的固定數字，避免結果出現重複的三元組
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 3. 在固定 nums[i] 的情況下，使用雙指針尋找剩下的兩個數
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    # 和太小，左指針往右移以增加數值
                    left += 1
                elif total > 0:
                    # 和太大，右指針往左移以減少數值
                    right -= 1
                else:
                    # 找到了符合條件的三元組
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # 關鍵：找到答案後，跳過左右指針指向的重複數字
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 兩邊指針同時收縮
                    left += 1
                    right -= 1
                    
        return res
```
---
Source: notebooklm-source/0016-3Sum-Closest.md

# 0016 - 3Sum Closest (最接近的三數之和)

## 1. 題目理解 (Problem Comprehension)

給你一個包含 `n` 個整數的陣列 `nums` 和一個目標值 `target`。請從 `nums` 中找出三個整數，使得它們的和與 `target` 最接近。

返回這三個整數的和。

**輸入與輸出格式：**
*   **輸入 (Input):**
    *   `nums`: 整數列表。
    *   `target`: 目標值。
*   **輸出 (Output):** 最接近 `target` 的三數之和。

**假設：**
*   每組輸入都恰好只有一個解。

**範例：**
`nums = [-1, 2, 1, -4], target = 1`
輸出: `2` (因為 `-1 + 2 + 1 = 2`，最接近 1)

## 2. 思路分析 (Thought Process)

這道題是 `0015 - 3Sum` 的變體。在 3Sum 中我們是在找等於 0 的組合，而這裡我們是在找「距離最小」的組合。

**優化思路：排序 + 雙指針**
同樣地，我們可以利用排序來簡化問題：
1.  **排序**：將陣列由小到大排序。
2.  **固定一個數**：遍歷陣列中的 `nums[i]`。
3.  **雙指針尋找**：在剩下的區間中使用 `left` 和 `right` 指針。
4.  **更新最接近值**：
    *   計算 `current_sum = nums[i] + nums[left] + nums[right]`。
    *   如果 `abs(current_sum - target)` 比目前記錄的最小差距還小，則更新結果。
    *   根據 `current_sum` 與 `target` 的大小關係來移動指針：
        *   `current_sum < target`：我們需要更大的和，所以 `left++`。
        *   `current_sum > target`：我們需要更小的和，所以 `right--`。
        *   `current_sum == target`：直接返回結果，因為差距為 0 是最完美的。

## 3. 演算法設計 (Algorithm Design)

我們採用 **排序 + 雙指針** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function threeSumClosest(nums, target):
    Sort nums
    closest_sum = nums[0] + nums[1] + nums[2]
    
    For i from 0 to n - 3:
        left = i + 1
        right = n - 1
        While left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            If current_sum == target:
                Return current_sum
            
            If abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
                
            If current_sum < target:
                left++
            Else:
                right--
                
    Return closest_sum
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N^2)**
    *   排序需要 O(N log N)。
    *   外部迴圈跑 N 次，內部雙指針跑 N 次。
*   **空間複雜度 (Space Complexity): O(1)** (或排序所需的 O(N))。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 1. 排序是雙指針法的基礎
        nums.sort()
        n = len(nums)
        # 初始化為前三個數的和
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # 2. 遍歷並固定第一個數
        for i in range(n - 2):
            # 優化：跳過重複的數
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 3. 使用雙指針在剩餘範圍尋找
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # 如果剛好等於 target，直接返回
                if current_sum == target:
                    return current_sum
                
                # 更新最接近的累計和
                # 如果當前和與目標的差距，小於之前記錄的差距
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # 4. 根據大小關係移動指針
                if current_sum < target:
                    # 當前和小了，左指針往右移來增加總和
                    left += 1
                else:
                    # 當前和大了，右指針往左移來減小總和
                    right -= 1
                    
        return closest_sum
```

---
Source: notebooklm-source/0017-Letter-Combinations-of-a-Phone-Number.md

# 0017 - Letter Combinations of a Phone Number (電話號碼的字母組合)

## 1. 題目理解 (Problem Comprehension)

給定一個僅包含數字 `2-9` 的字串，返回所有它能表示的字母組合。答案可以按 **任意順序** 返回。

給出數字到字母的映射（與電話按鍵相同）：
*   2: abc, 3: def, 4: ghi, 5: jkl, 6: mno, 7: pqrs, 8: tuv, 9: wxyz

**輸入與輸出格式：**
*   **輸入 (Input):** `digits`: 一個由數字組成的字串。
*   **輸出 (Output):** 字串列表，包含所有可能的組合。

**範例：**
`digits = "23"`
輸出: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

## 2. 思路分析 (Thought Process)

這是一個典型的組合問題。我們需要從第一個數字對應的字母中選一個，再從第二個數字選一個...以此類推。

當我們需要窮舉所有可能的「路徑」或「組合」時，**回溯演算法 (Backtracking)** 是最合適的工具。

**回溯法的核心思想：**
1.  **選擇**：從當前數字對應的字母集中選一個字母。
2.  **遞迴**：移動到下一個數字，繼續選擇。
3.  **撤銷（回溯）**：當完成一條路徑後，回到上一步，改選另一個字母。

## 3. 演算法設計 (Algorithm Design)

我們採用 **深度優先搜尋 (DFS) / 回溯法**。

**偽代碼 (Pseudo-code):**

```text
Function letterCombinations(digits):
    If digits is empty, return []
    
    Map phone = {2: "abc", 3: "def", ...}
    res = []
    
    Function backtrack(index, current_path):
        # 終止條件：如果路徑長度等於數字長度
        If length(current_path) == length(digits):
            Add current_path to res
            Return
            
        # 取得當前數字對應的所有字母
        letters = phone[digits[index]]
        For each char in letters:
            # 遞迴處理下一個數字
            backtrack(index + 1, current_path + char)
            
    backtrack(0, "")
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(3^N * 4^M)**
    *   N 是對應 3 個字母的數字個數，M 是對應 4 個字母的數字個數。
    *   總組合數就是這個複雜度。
*   **空間複雜度 (Space Complexity): O(N+M)**
    *   主要是遞迴堆疊的深度。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 如果輸入為空，直接返回空列表
        if not digits:
            return []
            
        # 建立電話按鍵的對照表
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        res = []
        
        # 定義回溯函式
        # index: 目前處理到第幾個數字
        # current_path: 目前累積的字母組合
        def backtrack(index: int, current_path: str):
            # 1. 終止條件：如果累積的組合長度等於輸入的數字長度
            if len(current_path) == len(digits):
                res.append(current_path)
                return
            
            # 2. 取得當前數字對應的候選字母
            possible_letters = phone_map[digits[index]]
            
            # 3. 遍歷候選字母
            for letter in possible_letters:
                # 進入下一層遞迴，處理下一個數字
                backtrack(index + 1, current_path + letter)
                
        # 從第 0 個數字、空組合開始搜尋
        backtrack(0, "")
        return res
```

---
Source: notebooklm-source/0018-4Sum.md

# 0018 - 4Sum (四數之和)

## 1. 題目理解 (Problem Comprehension)

給你一個由 `n` 個整數組成的陣列 `nums` ，和一個目標值 `target` 。

請你找出並返回滿足下述全部條件的所有**不重複**四元組 `[nums[a], nums[b], nums[c], nums[d]]` ：
*   `0 <= a, b, c, d < n`
*   `a, b, c, d` 互不相同
*   `nums[a] + nums[b] + nums[c] + nums[d] == target`

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 整數列表, `target`: 目標值。
*   **輸出 (Output):** 四元組列表。

**範例：**
`nums = [1, 0, -1, 0, -2, 2], target = 0`
輸出: `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`

## 2. 思路分析 (Thought Process)

這道題是 `3Sum` 的進階版。核心思路非常相似：**排序 + 多層迴圈 + 最內層雙指針**。

**策略：**
1.  **排序**：將陣列由小到大排序。
2.  **固定前兩個數**：
    *   第一層迴圈固定 `nums[i]`。
    *   第二層迴圈固定 `nums[j]` (從 `i+1` 開始)。
3.  **雙指針尋找後兩個數**：
    *   在 `[j+1, n-1]` 範圍內，使用 `left` 和 `right` 指針。
    *   尋找滿足 `nums[i] + nums[j] + nums[left] + nums[right] == target` 的組合。
4.  **去重**：在每一層迴圈中，如果當前的數字與前一個數字相同，則跳過。

### 優化技巧 (剪枝)
由於陣列已經排序，我們可以加入一些邏輯提早結束不必要的計算：
*   **如果目前最小的四數之和都大於 target**：剩下的組合只會更大，直接 `break`。
*   **如果目前最大的四數之和都小於 target**：目前的 `i` 或 `j` 太小了，直接 `continue` 到下一個。

## 3. 演算法設計 (Algorithm Design)

我們採用 **兩層迴圈 + 雙指針**。

**偽代碼 (Pseudo-code):**

```text
Function fourSum(nums, target):
    Sort nums
    res = []
    
    For i from 0 to n - 4:
        # 去重
        If i > 0 and nums[i] == nums[i-1]: Continue
        
        # 剪枝優化...
        
        For j from i + 1 to n - 3:
            # 去重
            If j > i + 1 and nums[j] == nums[j-1]: Continue
            
            # 雙指針
            left = j + 1
            right = n - 1
            While left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                If total == target:
                    Add to res
                    # 去重並收縮指針
                    ...
                Else if total < target:
                    left++
                Else:
                    right--
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N^3)**
    *   兩層迴圈加上一層雙指針。
*   **空間複雜度 (Space Complexity): O(1)** (或排序所需的 O(N))。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 1. 排序是處理不重複組合的關鍵
        nums.sort()
        n = len(nums)
        res = []
        
        # 2. 第一層迴圈：固定第一個數
        for i in range(n - 3):
            # 跳過重複的數字
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # [優化] 如果目前最小的四個數相加都大於目標，後面沒戲了
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # [優化] 如果目前數字加上最大的三個數都還小於目標，則當前 i 太小
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
                
            # 3. 第二層迴圈：固定第二個數
            for j in range(i + 1, n - 2):
                # 跳過重複的數字
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # [優化] 針對 j 的剪枝
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                
                # 4. 雙指針法：尋找最後兩個數
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        # 找到一組解
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        # 跳過重複的左指針和右指針
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                        
        return res
```

---
Source: notebooklm-source/0019-Remove-Nth-Node-From-End-of-List.md

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

---
Source: notebooklm-source/0020-Valid-Parentheses.md

# 0020 - Valid Parentheses (有效的括號)

## 1. 題目理解 (Problem Comprehension)

給定一個只包括 `'('`, `')'`, `'{'`, `'}'`, `'['`, `']'` 的字串 `s` ，判斷字串是否有效。

**有效字串需滿足：**
1.  左括號必須用相同類型的右括號閉合。
2.  左括號必須以正確的順序閉合。
3.  每個右括號都有一個對應的相同類型的左括號。

**輸入與輸出格式：**
*   **輸入 (Input):** `s`: 字串。
*   **輸出 (Output):** `True` 或 `False` (bool)。

**範例：**
*   `"()"` -> `True`
*   `"()[]{}"` -> `True`
*   `"(]"` -> `False`
*   `"([)]"` -> `False`
*   `"{[]}"` -> `True`

## 2. 思路分析 (Thought Process)

這是一個典型的「後進先出 (LIFO)」問題。最後一個出現的左括號，必須第一個被閉合。

**優化思路：堆疊 (Stack)**
我們可以使用一個 **堆疊 (Stack)** 來追蹤尚未閉合的左括號。

**步驟：**
1.  建立一個空的堆疊。
2.  遍歷字串中的每個字符：
    *   如果是 **左括號** (`(`, `{`, `[`):
        *   將它推入 (push) 堆疊。
    *   如果是 **右括號** (`)`, `}`, `]`):
        *   檢查堆疊是否為空？如果為空，表示沒有對應的左括號，無效。
        *   彈出 (pop) 堆疊頂端的左括號。
        *   檢查這個彈出的左括號是否與當前的右括號匹配？如果不匹配，無效。
3.  遍歷結束後，檢查堆疊是否為空：
    *   如果為空，表示所有左括號都正確閉合了，有效。
    *   如果不為空，表示有孤單的左括號，無效。

## 3. 演算法設計 (Algorithm Design)

我們採用 **堆疊 (Stack)** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function isValid(s):
    Initialize stack = []
    Initialize mapping = {')': '(', '}': '{', ']': '['}
    
    For each char in s:
        If char is a closing bracket (in mapping):
            If stack is empty:
                Return False
            top_element = stack.pop()
            If top_element != mapping[char]:
                Return False
        Else:
            # It's an opening bracket
            stack.push(char)
            
    Return stack is empty
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   我們只需要遍歷一次字串。每個字符的進棧和出棧操作都是 O(1)。
*   **空間複雜度 (Space Complexity): O(N)**
    *   在最壞情況下（全是左括號），我們需要將所有字符存入堆疊。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        # 如果字串長度是奇數，一定無法配對成功
        if len(s) % 2 != 0:
            return False
            
        # 建立一個映射表，方便我們根據右括號找到對應的左括號
        # 也可以反過來存，邏輯正確即可
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # 建立堆疊，用來存放還沒被閉合的左括號
        stack = []
        
        for char in s:
            # 如果目前字符是右括號
            if char in bracket_map:
                # 彈出堆疊頂端的元素（如果堆疊為空，給一個虛擬字符 '#'）
                top_element = stack.pop() if stack else '#'
                
                # 檢查彈出的左括號是否與當前的右括號匹配
                if bracket_map[char] != top_element:
                    return False
            else:
                # 如果是左括號，將它推入堆疊
                stack.append(char)
                    
        # 最後檢查堆疊是否為空。如果為空，代表所有的括號都完美配對
        return len(stack) == 0
```

---
Source: notebooklm-source/0021-Merge-Two-Sorted-Lists.md

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

---
Source: notebooklm-source/0022-Generate-Parentheses.md

# 0022 - Generate Parentheses (生成括號)

## 1. 題目理解 (Problem Comprehension)

數字 `n` 代表括號的對數，請你設計一個函式，用於能夠生成所有可能的並且 **有效的** 括號組合。

**輸入與輸出格式：**
*   **輸入 (Input):** `n`: 括號的對數 (int)。
*   **輸出 (Output):** 所有有效的括號組合列表 (List[str])。

**範例：**
輸入: `n = 3`
輸出: `["((()))","(()())","(())()","()(())","()()()"]`

## 2. 思路分析 (Thought Process)

這是一個典型的窮舉所有可能組合的問題。對於每個位置，我們都有兩個選擇：放一個左括號 `(` 或者放一個右括號 `)`。

**但是，不是所有的組合都是有效的。如何確保有效？**
1.  **左括號的數量**：最多只能放 `n` 個左括號。
2.  **右括號的數量**：在任何時候，已放置的右括號數量不能超過左括號的數量（否則就會出現像 `())` 這樣無法匹配的情況）。

**優化思路：回溯演算法 (Backtracking)**
我們可以使用遞迴來構建字串，並在每一步根據上述規則進行「剪枝」（即只走合法的路徑）。

## 3. 演算法設計 (Algorithm Design)

我們採用 **回溯法**。

**偽代碼 (Pseudo-code):**

```text
Function generateParenthesis(n):
    res = []
    
    Function backtrack(current_s, open_count, close_count):
        # 終止條件：如果字串長度達到 2*n
        If length(current_s) == 2 * n:
            Add current_s to res
            Return
            
        # 如果左括號還沒用完，可以放左括號
        If open_count < n:
            backtrack(current_s + "(", open_count + 1, close_count)
            
        # 如果右括號比左括號少，可以放右括號
        If close_count < open_count:
            backtrack(current_s + ")", open_count, close_count + 1)
            
    backtrack("", 0, 0)
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(4^n / sqrt(n))**
    *   這與卡特蘭數 (Catalan Number) 有關，代表了有效括號組合的數量。
*   **空間複雜度 (Space Complexity): O(n)**
    *   主要是遞迴堆疊的深度。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        # 定義回溯函式
        # current_s: 目前構建中的字串
        # open_count: 已經使用的左括號數量
        # close_count: 已經使用的右括號數量
        def backtrack(current_s: str, open_count: int, close_count: int):
            # 1. 終止條件：當字串長度達到 2 * n 時，表示一組完整的組合已生成
            if len(current_s) == 2 * n:
                res.append(current_s)
                return
            
            # 2. 選擇放左括號：
            # 只要左括號的使用數量還沒達到 n，就可以繼續放
            if open_count < n:
                backtrack(current_s + '(', open_count + 1, close_count)
            
            # 3. 選擇放右括號：
            # 關鍵規則：右括號的數量必須小於目前的左括號數量
            # 這樣才能保證每一個右括號都能找到對應的左括號
            if close_count < open_count:
                backtrack(current_s + ')', open_count, close_count + 1)
                
        # 從空字串、0 個左括號、0 個右括號開始遞迴
        backtrack("", 0, 0)
        return res
```

---
Source: notebooklm-source/0023-Merge-k-Sorted-Lists.md

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

---
Source: notebooklm-source/0024-Swap-Nodes-in-Pairs.md

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

---
Source: notebooklm-source/0025-Reverse-Nodes-in-k-Group.md

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

---
Source: notebooklm-source/0026-Remove-Duplicates-from-Sorted-Array.md

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

---
Source: notebooklm-source/0027-Remove-Element.md

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

---
Source: notebooklm-source/0028-Find-the-Index-of-the-First-Occurrence-in-a-String.md

# 0028 - Find the Index of the First Occurrence in a String (找出字串中第一個匹配項的下標)

## 1. 題目理解 (Problem Comprehension)

給你兩個字串 `haystack` 和 `needle` ，請你在 `haystack` 字串中找出 `needle` 字串出現的第一個位置（下標從 0 開始）。如果 `needle` 不是 `haystack` 的一部分，則返回 `-1` 。

**輸入與輸出格式：**
*   **輸入 (Input):** `haystack`: 主字串, `needle`: 待尋找的子字串。
*   **輸出 (Output):** 第一個匹配的索引 (int)。

**範例：**
輸入: `haystack = "sadbutsad", needle = "sad"`
輸出: `0`

## 2. 思路分析 (Thought Process)

這道題在傳統電腦科學中被稱為「字串搜索」問題。

### 直觀解法：滑動窗口 (Sliding Window)
我們想像一個長度與 `needle` 相同的窗口，在 `haystack` 上從左往右滑動。
1.  窗口的起點 `i` 從 0 開始，直到 `len(haystack) - len(needle)`。
2.  在每個起點，檢查從 `i` 開始、長度為 `m` 的子串是否等於 `needle`。
3.  如果相等，直接返回 `i`。
4.  如果遍歷完都沒有找到，返回 -1。

### 進階解法：KMP 演算法
雖然滑動窗口足以應付這題，但在面試中，面試官可能會問你如何優化。**KMP (Knuth-Morris-Pratt)** 演算法可以在 O(N) 的時間內完成搜索，它利用了 `needle` 本身的重複特徵來避免不必要的重複比較。不過對於初學者來說，先掌握滑動窗口法是最基礎且重要的。

## 3. 演算法設計 (Algorithm Design)

我們採用 **滑動窗口 (Slicing)**。

**偽代碼 (Pseudo-code):**

```text
Function strStr(haystack, needle):
    If needle is empty, return 0
    
    n = length(haystack)
    m = length(needle)
    
    For i from 0 to n - m:
        # 檢查 haystack 從 i 開始長度為 m 的子串
        If haystack[i...i+m-1] == needle:
            Return i
            
    Return -1
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O((N-M) * M)**
    *   N 是 `haystack` 的長度，M 是 `needle` 的長度。在最壞的情況下（如 `haystack = "aaaaa", needle = "aab"`），我們需要進行多次比較。
*   **空間複雜度 (Space Complexity): O(1)**
    *   在 Python 中，切片 `haystack[i:i+m]` 會產生一個新字串，這在空間上是 O(M)，但我們只是用來比較，不會長期儲存。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 1. 根據題目規範，如果 needle 是空字串，返回 0
        if not needle:
            return 0
            
        n = len(haystack)
        m = len(needle)
        
        # 2. 開始在 haystack 中滑動窗口
        # 迴圈範圍只需到 n - m，因為剩下的長度如果比 needle 短，就不可能匹配
        # +1 是因為 range 不包含結尾
        for i in range(n - m + 1):
            # 3. 提取從 i 開始、長度與 needle 相同的子串
            # 並檢查它是否等於 needle
            # 在 Python 中，字串切片 s[start:end] 非常高效且易讀
            if haystack[i : i + m] == needle:
                # 如果匹配成功，這就是我們要找的第一個出現位置
                return i
                
        # 4. 如果整個迴圈跑完都沒有發現匹配項
        return -1
```

---
Source: notebooklm-source/0029-Divide-Two-Integers.md

# 0029 - Divide Two Integers (兩數相除)

## 1. 題目理解 (Problem Comprehension)

給你兩個整數，被除數 `dividend` 和除數 `divisor`。將兩數相除，但**不得使用**乘法、除法和取餘運算子。

返回被除數除以除數得到的商。

**規則：**
1.  整數除法應該向零截斷，也就是說丟棄小數部分。
2.  假設環境只能存儲 32 位元有號整數 `[-2^31, 2^31 - 1]`。
3.  如果除法結果溢出，返回 `2^31 - 1`。

**輸入與輸出格式：**
*   **輸入 (Input):** `dividend`, `divisor` (int)。
*   **輸出 (Output):** 商 (int)。

**範例：**
輸入: `dividend = 10, divisor = 3`
輸出: `3` (10 / 3 = 3.333...，截斷為 3)

## 2. 思路分析 (Thought Process)

不能用乘除法，我們最直覺的想法是用「減法」：看被除數裡面可以減去幾個除數。
但如果 `dividend` 是 21 億，`divisor` 是 1，我們要減 21 億次，這太慢了。

**優化思路：位元運算 (Bit Manipulation)**
我們可以使用「倍增」的思想。與其一個一個減，不如一組一組減。
我們可以利用位元左移 `<<` 來實現乘以 2。

**步驟：**
1.  **處理符號**：記錄結果的正負號，並將兩數轉為正數處理。
2.  **倍增除數**：
    *   假設 `a = 100`, `b = 3`。
    *   `3 << 1 = 6` (3 * 2)
    *   `6 << 1 = 12` (3 * 4)
    *   `12 << 1 = 24` (3 * 8)
    *   `24 << 1 = 48` (3 * 16)
    *   `48 << 1 = 96` (3 * 32)
    *   現在 `96` 很接近 `100` 了。我們從 `100` 中減去 `96`，結果加上 `32`。
    *   剩下 `4`，重複上述過程，`4` 裡面還有一個 `3`，結果加 `1`。
    *   最後結果 `32 + 1 = 33`。
3.  **處理邊界**：確保結果在 32 位元範圍內。

## 3. 演算法設計 (Algorithm Design)

我們採用 **倍增減法 (Exponential Search style)**。

**偽代碼 (Pseudo-code):**

```text
Function divide(dividend, divisor):
    If dividend == MIN and divisor == -1: return MAX
    
    sign = (dividend > 0) == (divisor > 0)
    a = abs(dividend)
    b = abs(divisor)
    res = 0
    
    While a >= b:
        temp_b = b
        multiple = 1
        While a >= (temp_b << 1):
            temp_b = temp_b << 1
            multiple = multiple << 1
            
        a = a - temp_b
        res = res + multiple
        
    Return sign ? res : -res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O((log N)^2)**
    *   外部迴圈減少了 `a`，內部迴圈尋找最大的倍數。這比直接減法快得多。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 定義 32 位元整數的邊界
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        # 特殊情況：溢位處理
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
            
        # 1. 判斷最終結果的正負號
        # 如果兩者同號，結果為正；異號則為負
        is_positive = (dividend > 0) == (divisor > 0)
        
        # 全部轉為正數進行計算
        a, b = abs(dividend), abs(divisor)
        res = 0
        
        # 2. 核心邏輯：使用位移來實現快速減法
        while a >= b:
            # temp_b 會不斷翻倍 (3, 6, 12, 24...)
            # count 也會同步翻倍 (1, 2, 4, 8...)
            temp_b, count = b, 1
            
            # 只要 a 還大於等於 temp_b 的兩倍，就繼續翻倍
            # 這裡的 (temp_b << 1) 相當於 temp_b * 2
            while a >= (temp_b << 1):
                temp_b <<= 1
                count <<= 1
                
            # 減去目前能找到的最大倍數
            a -= temp_b
            # 將對應的商累加到結果
            res += count
            
        # 3. 恢復正負號
        res = res if is_positive else -res
        
        # 4. 最後檢查是否在 32 位元範圍內並返回
        if res < MIN_INT: return MIN_INT
        if res > MAX_INT: return MAX_INT
        return res
```

---
Source: notebooklm-source/0030-Substring-with-Concatenation-of-All-Words.md

# 0030 - Substring with Concatenation of All Words (串聯所有單詞的子串)

## 1. 題目理解 (Problem Comprehension)

這是一道 LeetCode 的 **Hard** 題目。
給你一個字串 `s` 和一個字串陣列 `words`。`words` 中所有字串的**長度都相同**。

一個「串聯子串」是指包含 `words` 中所有字串（以任意順序排列）連接而成的子串，且中間沒有任何其他字符。

請返回 `s` 中所有這類串聯子串的起始索引。

**輸入與輸出格式：**
*   **輸入 (Input):** `s`: 字串, `words`: 字串列表。
*   **輸出 (Output):** 起始索引列表 (List[int])。

**範例：**
`s = "barfoothefoobarman"`, `words = ["foo","bar"]`
輸出: `[0, 9]`
（索引 0 是 "barfoo"，索引 9 是 "foobar"）

## 2. 思路分析 (Thought Process)

這道題的關鍵在於 `words` 中每個單詞的長度 `L` 是固定的。

### 直觀解法：滑動窗口 + 哈希表
我們可以在 `s` 中檢查每一個可能的起點 `i`，看從 `i` 開始長度為 `L * num_words` 的子串是否符合要求。
這需要 O(N * num_words) 的時間，效率稍低。

### 優化思路：移動窗口 (Sliding Window)
既然單詞長度固定為 `L`，我們其實只需要運行 `L` 次滑動窗口。
*   第一次窗口從索引 0 開始，每次移動 `L` 個字符。
*   第二次窗口從索引 1 開始，每次移動 `L` 個字符。
*   ...
*   第 L 次窗口從索引 `L-1` 開始。

在每一次滑動窗口中：
1.  我們用一個 `Counter` 來記錄當前窗口內各個單詞出現的次數。
2.  用一個 `left` 和 `right` 指針來維護窗口。
3.  如果新加入的單詞在 `words` 中：
    *   增加計數。
    *   如果該單詞出現次數超過了 `words` 中的限制，則收縮 `left` 指針直到次數恢復正常。
    *   如果窗口內的單詞總數等於 `num_words`，記錄 `left` 為一個解。
4.  如果新加入的單詞不在 `words` 中：
    *   清空當前計數，將 `left` 移到 `right` 的下一個位置。

## 3. 演算法設計 (Algorithm Design)

我們採用 **多起點滑動窗口**。

**偽代碼 (Pseudo-code):**

```text
Function findSubstring(s, words):
    word_len = length(words[0])
    num_words = length(words)
    word_count = Counter(words)
    res = []
    
    For i from 0 to word_len - 1:
        left = i
        right = i
        current_count = Counter()
        
        While right + word_len <= length(s):
            word = s[right : right + word_len]
            right += word_len
            
            If word in word_count:
                current_count[word]++
                While current_count[word] > word_count[word]:
                    left_word = s[left : left + word_len]
                    current_count[left_word]--
                    left += word_len
                
                If (right - left) / word_len == num_words:
                    Add left to res
            Else:
                current_count.clear()
                left = right
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   其中 N 是字串 `s` 的長度。雖然有 `word_len` 次循環，但每次循環中指針 `left` 和 `right` 都只會遍歷一次字串。
*   **空間複雜度 (Space Complexity): O(M)**
    *   M 是 `words` 的大小，用於儲存哈希表。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
            
        word_len = len(words[0])   # 每個單詞的固定長度
        num_words = len(words)     # 單詞的總個數
        word_count = Counter(words) # 統計 words 中各單詞應有的次數
        res = []
        
        # 為什麼要遍歷 word_len 次？
        # 因為我們的窗口每次跳 word_len，所以要分別從 0, 1, ..., word_len-1 開始
        # 才能覆蓋到所有可能的起始位置
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter() # 記錄目前窗口內的單詞次數
            words_used = 0           # 目前窗口內的總單詞數
            
            # 向右滑動窗口
            while right + word_len <= len(s):
                # 截取一個單詞
                word = s[right : right + word_len]
                right += word_len
                
                # 如果這個單詞在目標 words 列表中
                if word in word_count:
                    current_count[word] += 1
                    words_used += 1
                    
                    # 如果目前的單詞次數超過了規定的次數
                    # 不斷移動左邊界，直到次數恢復正常
                    while current_count[word] > word_count[word]:
                        left_word = s[left : left + word_len]
                        current_count[left_word] -= 1
                        words_used -= 1
                        left += word_len
                    
                    # 如果窗口內的單詞數正好等於總單詞數，說明找到了一個匹配
                    if words_used == num_words:
                        res.append(left)
                else:
                    # 如果遇到一個根本不在 words 列表中的單詞
                    # 之前的努力全白費，清空計數並重置左邊界
                    current_count.clear()
                    words_used = 0
                    left = right
                    
        return res
```

---
Source: notebooklm-source/0031-Next-Permutation.md

# 0031 - Next Permutation (下一個排列)

## 1. 題目理解 (Problem Comprehension)

給你一個整數陣列 `nums` ，找出 `nums` 的下一個字典序更大的排列。

如果不存在下一個更大的排列（即目前的排列已經是最大的，如 `[3, 2, 1]`），則將陣列重排成最小的排列（即升序排列，如 `[1, 2, 3]`）。

**要求：**
*   必須 **原地 (In-place)** 修改。
*   只能使用額外的常數空間。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 整數列表。
*   **輸出 (Output):** 無（直接修改 `nums`）。

**範例：**
`[1, 2, 3]` -> `[1, 3, 2]`
`[3, 2, 1]` -> `[1, 2, 3]`
`[1, 1, 5]` -> `[1, 5, 1]`

## 2. 思路分析 (Thought Process)

我們需要找到一個比當前排列「大一點點」的排列。

**演算法步驟：**
1.  **從右往左找第一個「下降點」**：
    *   找到第一個滿足 `nums[i] < nums[i+1]` 的索引 `i`。
    *   如果找不到（即整個陣列是降序的），說明這是最大排列，直接跳到第 4 步翻轉整個陣列。
2.  **從右往左找第一個「剛好大於 `nums[i]` 的數」**：
    *   在 `i` 的右側（這部分目前是降序的），找到第一個滿足 `nums[j] > nums[i]` 的索引 `j`。
3.  **交換 `nums[i]` 和 `nums[j]`**：
    *   這樣我們在 `i` 位置放了一個稍大一點的數。
4.  **反轉 `i` 之後的部分**：
    *   因為 `i` 之後的部分原本是降序的，反轉後會變成升序，這能保證我們得到的排列是所有「大於原排列」中最小的那一個（即「下一個」）。

## 3. 演算法設計 (Algorithm Design)

我們採用 **標準下一個排列演算法**。

**偽代碼 (Pseudo-code):**

```text
Function nextPermutation(nums):
    n = length(nums)
    i = n - 2
    
    # 1. 找下降點
    While i >= 0 and nums[i] >= nums[i+1]:
        i = i - 1
        
    If i >= 0:
        # 2. 找剛好大的數
        j = n - 1
        While j >= 0 and nums[j] <= nums[i]:
            j = j - 1
        # 3. 交換
        Swap(nums, i, j)
        
    # 4. 反轉後面的部分
    Reverse(nums, i + 1, n - 1)
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   我們最多遍歷兩次陣列，並進行一次反轉操作。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # 1. 從右往左尋找第一個「升序對」 (nums[i] < nums[i+1])
        # 這意味著 i 之後的部分都是降序的
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        # 如果找到了這樣的 i (即 i >= 0)
        if i >= 0:
            # 2. 在右側的降序序列中，從右往左找到第一個比 nums[i] 大的數
            # 這個數是所有比 nums[i] 大的數中最小的一個
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            
            # 3. 交換這兩個數
            # 現在 i 位置變大了一點點
            nums[i], nums[j] = nums[j], nums[i]
            
        # 4. 關鍵一步：將 i 之後的部分反轉
        # 既然 i 之後原本是降序的，反轉後就會變成最小的升序排列
        # 這樣才能確保我們得到的是「下一個」緊鄰的較大排列
        self.reverse(nums, i + 1, n - 1)
        
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        # 輔助函式：原地反轉陣列的部分區間
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
```

---
Source: notebooklm-source/0032-Longest-Valid-Parentheses.md

# 0032 - Longest Valid Parentheses (最長有效括號)

## 1. 題目理解 (Problem Comprehension)

給你一個只包含 `'('` 和 `')'` 的字串，找出最長的包含有效括號的子串的長度。

這是一道 LeetCode 的 **Hard** 題目。

**輸入與輸出格式：**
*   **輸入 (Input):** `s`: 只包含 `(` 和 `)` 的字串。
*   **輸出 (Output):** 最長有效子串的長度 (int)。

**範例：**
1.  `"(()"` -> `2` (有效子串是 "()")
2.  `")()())"` -> `4` (有效子串是 "()()")
3.  `""` -> `0`

## 2. 思路分析 (Thought Process)

這題可以用動態規劃 (DP) 或堆疊 (Stack) 來解決。我們這裡介紹更直觀的堆疊做法。

**優化思路：堆疊 (Stack) 記錄索引**
在一般的「判斷合法括號」問題中，我們只在堆疊裡放括號。但在這題中，我們要在堆疊裡放**索引 (Index)**，這樣我們才能計算長度。

**關鍵技巧：**
*   **初始化**：我們在堆疊中預先放入 `-1`。這是一個「參照點」，用來計算從字串開頭開始的有效長度。
*   **遇到 `(`**：將目前的索引 `i` 推入堆疊。
*   **遇到 `)`**：
    1.  彈出堆疊頂部元素。
    2.  如果堆疊變**空**了：說明這個 `)` 沒有匹配的左括號。我們將目前的索引 `i` 推入堆疊，作為新的「參照點」。
    3.  如果堆疊**不為空**：說明匹配成功了！目前的有效長度就是 `當前索引 i - 堆疊頂部元素`。更新最大長度。

## 3. 演算法設計 (Algorithm Design)

我們採用 **堆疊 (Stack)** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function longestValidParentheses(s):
    Initialize stack = [-1]
    Initialize max_len = 0
    
    For i, char in s:
        If char == '(':
            stack.push(i)
        Else:
            stack.pop()
            If stack is empty:
                # 無法配對，更新參照點
                stack.push(i)
            Else:
                # 配對成功，計算長度
                current_len = i - stack.top()
                max_len = max(max_len, current_len)
                
    Return max_len
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   只需要遍歷一次字串。
*   **空間複雜度 (Space Complexity): O(N)**
    *   在最壞情況下（全是左括號），堆疊的大小會達到 N。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 1. 建立一個堆疊，用來儲存括號的索引 (Index)
        # 初始化為 -1，這是一個「虛擬的最後一個不合法右括號的位置」
        # 它能幫助我們計算從字串開頭開始的有效長度
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # 2. 遇到左括號，將它的位置存入堆疊
                stack.append(i)
            else:
                # 3. 遇到右括號，先彈出最近的一個左括號索引
                stack.pop()
                
                if not stack:
                    # 如果彈出後堆疊變空了，說明這個右括號沒有匹配的左括號
                    # 我們將它作為新的「最後一個不合法位置」存入堆疊
                    stack.append(i)
                else:
                    # 如果堆疊不為空，說明配對成功了！
                    # 目前最長有效括號的長度 = 目前索引 - 堆疊頂部剩餘的索引
                    # 堆疊頂部的索引是「上一個沒被匹配的位置」
                    current_len = i - stack[-1]
                    if current_len > max_len:
                        max_len = current_len
                        
        return max_len
```

---
Source: notebooklm-source/0033-Search-in-Rotated-Sorted-Array.md

# 0033 - Search in Rotated Sorted Array (搜索旋轉排序陣列)

## 1. 題目理解 (Problem Comprehension)

整數陣列 `nums` 原本是按升序排列的，但在傳遞給函式之前，它在某個未知的下標 `k` 處進行了旋轉。
例如，`[0,1,2,4,5,6,7]` 可能變成 `[4,5,6,7,0,1,2]`。

給你旋轉後的陣列 `nums` 和一個目標值 `target` ，如果 `nums` 中存在這個目標值，則返回它的下標，否則返回 `-1` 。

**要求：**
*   演算法的時間複雜度必須是 **O(log n)**。這意味著我們必須使用二分搜尋的變體。
*   陣列中的值都是唯一的。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 旋轉後的有序列表, `target`: 目標值。
*   **輸出 (Output):** 目標值的索引 (int)。

## 2. 思路分析 (Thought Process)

雖然陣列被旋轉了，但它仍然是「局部有序」的。如果我們在中間切一刀，**左右兩半中至少有一半是完全有序的**。

**如何利用這個特點？**
1.  找到中間點 `mid`。
2.  判斷哪一邊是有序的：
    *   如果 `nums[left] <= nums[mid]`，代表**左半邊是有序的**。
    *   否則，**右半邊是有序的**。
3.  在有序的那一邊檢查 `target` 是否在範圍內：
    *   如果在，縮小範圍到那一邊。
    *   如果不在，縮小範圍到另一邊。

這個邏輯可以讓我們在每次比較中排除掉一半的元素，保持 O(log N) 的效率。

## 3. 演算法設計 (Algorithm Design)

我們採用 **二分搜尋法 (Binary Search)**。

**偽代碼 (Pseudo-code):**

```text
Function search(nums, target):
    left = 0, right = length(nums) - 1
    
    While left <= right:
        mid = (left + right) / 2
        If nums[mid] == target: Return mid
        
        # 判斷哪邊是有序的
        If nums[left] <= nums[mid]:
            # 左半邊有序
            If nums[left] <= target < nums[mid]:
                # target 在左邊
                right = mid - 1
            Else:
                # target 在右邊
                left = mid + 1
        Else:
            # 右半邊有序
            If nums[mid] < target <= nums[right]:
                # target 在右邊
                left = mid + 1
            Else:
                # target 在左邊
                right = mid - 1
    Return -1
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(log N)**
    *   標準的二分搜尋。
*   **空間複雜度 (Space Complexity): O(1)**

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
            
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # 1. 找到了直接返回
            if nums[mid] == target:
                return mid
            
            # 2. 關鍵：判斷哪一半邊是「有序」的
            # 因為是旋轉過的，兩邊一定有一邊是正常的升序
            if nums[left] <= nums[mid]:
                # 情況 A：左半邊 [left...mid] 是有序的
                # 檢查 target 是否落在這個有序區間內
                if nums[left] <= target < nums[mid]:
                    # 在區間內，將搜尋範圍縮小到左半邊
                    right = mid - 1
                else:
                    # 不在區間內，去右半邊找
                    left = mid + 1
            else:
                # 情況 B：右半邊 [mid...right] 是有序的
                # 檢查 target 是否落在這個有序區間內
                if nums[mid] < target <= nums[right]:
                    # 在區間內，將搜尋範圍縮小到右半邊
                    left = mid + 1
                else:
                    # 不在區間內，去左半邊找
                    right = mid - 1
                    
        # 3. 遍歷結束仍未找到
        return -1
```

---
Source: notebooklm-source/0034-Find-First-and-Last-Position-of-Element-in-Sorted-Array.md

# 0034 - Find First and Last Position of Element in Sorted Array (在排序陣列中查找元素的第一個和最後一個位置)

## 1. 題目理解 (Problem Comprehension)

給你一個按照非遞減順序排列的整數陣列 `nums`，以及一個目標值 `target`。請你找出給定目標值在陣列中的開始位置和結束位置。

如果陣列中不存在目標值 `target`，返回 `[-1, -1]`。

**要求：**
*   演算法的時間複雜度必須是 **O(log n)**。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 有序整數列表, `target`: 目標值。
*   **輸出 (Output):** 包含兩個整數的列表，代表起始與結束位置。

**範例：**
輸入: `nums = [5,7,7,8,8,10], target = 8`
輸出: `[3, 4]`

## 2. 思路分析 (Thought Process)

由於要求 O(log N) 的時間複雜度，我們直覺地想到二分搜尋法。普通的二分搜尋法只能幫我們找到「其中一個」目標值，但目標值可能有重複，分佈在一個區間內。

**優化思路：兩次二分搜尋**
我們可以分別尋找目標值的**左邊界**和**右邊界**。

1.  **尋找左邊界**：
    *   在標準二分搜尋中，當 `nums[mid] == target` 時，我們不立即停止，而是記錄下這個位置，並繼續往**左半邊**搜尋 (`right = mid - 1`)，看看還有沒有更靠左的 `target`。
2.  **尋找右邊界**：
    *   當 `nums[mid] == target` 時，我們記錄下這個位置，並繼續往**右半邊**搜尋 (`left = mid + 1`)，看看還有沒有更靠右的 `target`。

這樣通過兩次搜尋，我們就能準確鎖定 `target` 的範圍。

## 3. 演算法設計 (Algorithm Design)

我們採用 **改進的二分搜尋法**。

**偽代碼 (Pseudo-code):**

```text
Function searchRange(nums, target):
    start = findBound(nums, target, is_left=True)
    end = findBound(nums, target, is_left=False)
    Return [start, end]

Function findBound(nums, target, is_left):
    left = 0, right = length(nums) - 1
    bound = -1
    While left <= right:
        mid = (left + right) / 2
        If nums[mid] == target:
            bound = mid
            If is_left: right = mid - 1
            Else: left = mid + 1
        Else if nums[mid] > target:
            right = mid - 1
        Else:
            left = mid + 1
    Return bound
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(log N)**
    *   兩次獨立的二分搜尋，總共是 2 * log N。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 輔助函式：用二分搜尋法尋找邊界
        # is_left 為 True 時尋找最左邊的匹配位置，False 時尋找最右邊
        def findBound(is_left: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    # 找到了目標值，先記錄下目前的索引
                    bound = mid
                    # 關鍵：為了找到邊界，我們不停止搜尋
                    if is_left:
                        # 尋找左邊界，所以繼續往左半邊縮小範圍
                        right = mid - 1
                    else:
                        # 尋找右邊界，所以繼續往右半邊縮小範圍
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return bound
            
        # 分別呼叫兩次二分搜尋
        start = findBound(is_left=True)
        end = findBound(is_left=False)
        
        return [start, end]
```

---
Source: notebooklm-source/0035-Search-Insert-Position.md

# 0035 - Search Insert Position (搜索插入位置)

## 1. 題目理解 (Problem Comprehension)

給定一個排序陣列和一個目標值，在陣列中找到目標值，並返回其索引。如果目標值不存在於陣列中，返回它將會被按順序插入的位置。

**關鍵要求：**
*   陣列是排序好的。
*   陣列中沒有重複數字。
*   演算法的時間複雜度必須是 **O(log n)**。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 有序整數列表, `target`: 目標值。
*   **輸出 (Output):** 索引 (int)。

**範例：**
輸入: `[1, 3, 5, 6], 5` -> 輸出: `2`
輸入: `[1, 3, 5, 6], 2` -> 輸出: `1`

## 2. 思路分析 (Thought Process)

這是一道非常經典的二分搜尋法應用題。

**優化思路：二分搜尋 (Binary Search)**
我們可以使用標準的二分搜尋。當搜尋結束且沒有找到 `target` 時，**`left` 指針所在的位置，恰好就是該數字應該被插入的位置**。

**為什麼？**
當迴圈結束時，`left > right`。此時：
*   所有小於 `target` 的數都在 `left` 的左邊。
*   所有大於 `target` 的數都在 `left`（包含自己）的右邊。
所以 `left` 就是插入點。

## 3. 演算法設計 (Algorithm Design)

我們採用 **標準二分搜尋法**。

**偽代碼 (Pseudo-code):**

```text
Function searchInsert(nums, target):
    left = 0
    right = length(nums) - 1
    
    While left <= right:
        mid = (left + right) / 2
        If nums[mid] == target:
            Return mid
        Else if nums[mid] < target:
            left = mid + 1
        Else:
            right = mid - 1
            
    # 如果沒找到，left 就是插入位置
    Return left
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(log N)**
    *   標準二分搜尋。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 使用左右雙指針來進行二分搜尋
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # 取得中間索引
            mid = (left + right) // 2
            
            # 如果剛好等於目標值，直接返回索引
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # 如果中間值比目標小，代表目標在右半邊
                left = mid + 1
            else:
                # 如果中間值比目標大，代表目標在左半邊
                right = mid - 1
                
        # 關鍵點：當迴圈結束且未找到 target 時
        # left 指針會停在第一個「大於目標值」的元素位置上
        # 這正好就是 target 應該被插入的位置
        return left
```

---
Source: notebooklm-source/0036-Valid-Sudoku.md

# 0036 - Valid Sudoku (有效的數獨)

## 1. 題目理解 (Problem Comprehension)

請你判斷一個 9x9 的數獨板是否有效。只需要根據以下規則，驗證已經填入數字的格位：

1.  每一行必須包含數字 `1-9`，且不能重複。
2.  每一列必須包含數字 `1-9`，且不能重複。
3.  每一個 3x3 的九宮格（總共 9 個）也必須包含數字 `1-9`，且不能重複。

**注意：**
*   一個有效的數獨（尚未填滿）不一定是可解的。
*   只需要驗證已經填入的數字是否滿足上述規則。
*   空白格位以 `'.'` 表示。

## 2. 思路分析 (Thought Process)

我們需要檢查三種維度：行、列、九宮格。

**優化思路：一次遍歷 + 哈希集 (Sets)**
我們遍歷整個 9x9 的棋盤一次。對於每個格子 `(r, c)`：
1.  如果它是空的 (`.`)，跳過。
2.  如果它有數字 `val`：
    *   檢查第 `r` 行是否已經出現過 `val`？
    *   檢查第 `c` 列是否已經出現過 `val`？
    *   檢查所在的九宮格是否已經出現過 `val`？

**如何計算九宮格的索引？**
一個 9x9 的棋盤可以分成 9 個 3x3 的九宮格。
索引計算公式為：`box_index = (r // 3) * 3 + (c // 3)`。
*   例如：`(0,0)` 到 `(2,2)` 都在九宮格 0。
*   例如：`(0,3)` 到 `(2,5)` 都在九宮格 1。

我們可以使用 9 個 Set 來儲存每一行看過的數字，9 個 Set 給每一列，9 個 Set 給每個九宮格。

## 3. 演算法設計 (Algorithm Design)

我們採用 **哈希集 (HashSet)** 記錄。

**偽代碼 (Pseudo-code):**

```text
Function isValidSudoku(board):
    Initialize rows = list of 9 empty sets
    Initialize cols = list of 9 empty sets
    Initialize boxes = list of 9 empty sets
    
    For r from 0 to 8:
        For c from 0 to 8:
            val = board[r][c]
            If val == ".": Continue
            
            # 檢查行
            If val in rows[r]: Return False
            rows[r].add(val)
            
            # 檢查列
            If val in cols[c]: Return False
            cols[c].add(val)
            
            # 檢查九宮格
            box_idx = (r // 3) * 3 + (c // 3)
            If val in boxes[box_idx]: Return False
            boxes[box_idx].add(val)
            
    Return True
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(1)**
    *   雖然有嵌套迴圈，但棋盤大小固定為 9x9 = 81 個格子。操作次數是常數。
*   **空間複雜度 (Space Complexity): O(1)**
    *   儲存看過數字的 Set 大小也是固定的（最多 81 個元素）。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 建立 9 個集合來分別儲存每一行、每一列和每個九宮格中出現過的數字
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # 遍歷 9x9 棋盤的每一個格子
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # 如果是空格，則不需要檢查，跳到下一個
                if val == '.':
                    continue
                
                # 1. 檢查目前行是否重複
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                # 2. 檢查目前列是否重複
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                # 3. 檢查目前所在的 3x3 九宮格是否重複
                # box_idx 計算方式：將 9x9 切成 3x3 個大區塊
                # (r // 3) 決定是大區塊的第幾橫排 (0, 1, 2)
                # (c // 3) 決定是大區塊的第幾直排 (0, 1, 2)
                box_idx = (r // 3) * 3 + (c // 3)
                if val in boxes[box_idx]:
                    return False
                boxes[box_idx].add(val)
                
        # 如果所有格子都檢查完畢且沒發現重複，則是有效的數獨
        return True
```

---
Source: notebooklm-source/0037-Sudoku-Solver.md

# 0037 - Sudoku Solver (解數獨)

## 1. 題目理解 (Problem Comprehension)

編寫一個程式，透過填充空白格位來解決數獨問題。

一個數獨的解法需遵循以下規則：
1.  數字 `1-9` 在每一行只能出現一次。
2.  數字 `1-9` 在每一列只能出現一次。
3.  數字 `1-9` 在每一個以粗實線分隔的 3x3 九宮格內只能出現一次。

空白格位用 `'.'` 表示。

這是一道 LeetCode 的 **Hard** 題目。

**輸入與輸出格式：**
*   **輸入 (Input):** `board`: 9x9 的字串二維列表。
*   **輸出 (Output):** 無（直接修改 `board`）。

## 2. 思路分析 (Thought Process)

這是一個經典的搜索問題。我們需要填滿所有的空白格，且每一步的選擇都要滿足數獨規則。

**優化思路：回溯演算法 (Backtracking)**
回溯法是一種「試錯」的搜尋策略：
1.  **尋找空格**：找到棋盤上第一個還沒填數字的地方。
2.  **嘗試填入**：依序嘗試填入 `1` 到 `9`。
3.  **合法性檢查**：在填入某個數字前，檢查它是否與目前的行、列、九宮格衝突。
4.  **繼續搜尋**：如果填入合法，就遞迴地去解剩下的棋盤。
5.  **撤銷 (Backtrack)**：如果後面的棋盤解不出來（返回 False），代表目前這個數字選錯了。我們將目前格子恢復成 `'.'`，並嘗試下一個數字。
6.  **完成**：當沒有空格時，代表解題成功。

## 3. 演算法設計 (Algorithm Design)

我們採用 **深度優先搜尋 (DFS) / 回溯法**。

**偽代碼 (Pseudo-code):**

```text
Function solve(board):
    For each cell (r, c) in board:
        If board[r][c] == ".":
            For num from "1" to "9":
                If is_valid(board, r, c, num):
                    board[r][c] = num
                    If solve(board): Return True
                    board[r][c] = "."  # Backtrack
            Return False # 此格填什麼都不對，向上層返回
    Return True # 沒空格了，解完
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(9^m)**
    *   m 是空格的數量。雖然理論上限很高，但數獨的規則限制會剪掉絕大部分的分支，實際運行很快。
*   **空間複雜度 (Space Complexity): O(1)**
    *   直接修改原棋盤。遞迴深度最大為 81。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self._solve(board)

    def _solve(self, board: List[List[str]]) -> bool:
        # 1. 遍歷棋盤，尋找下一個空白格位 ('.')
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    # 2. 嘗試填入數字 1 到 9
                    for num in "123456789":
                        # 3. 檢查填入該數字是否合法
                        if self._is_valid(board, r, c, num):
                            # 做選擇：填入數字
                            board[r][c] = num
                            
                            # 遞迴：嘗試填寫下一個空格
                            if self._solve(board):
                                return True
                            
                            # 回溯：如果後續解不出來，撤銷目前的選擇，恢復成空白
                            board[r][c] = '.'
                    
                    # 4. 如果 1-9 都試過且都不行，說明目前的棋盤狀態無解
                    return False
        
        # 5. 如果遍歷完整個棋盤都沒有遇到 '.'，代表數獨已解完
        return True

    def _is_valid(self, board: List[List[str]], row: int, col: int, char: str) -> bool:
        # 檢查某一格填入 char 是否符合數獨規則
        for i in range(9):
            # 檢查同一行是否已有重複
            if board[row][i] == char:
                return False
            # 檢查同一列是否已有重複
            if board[i][col] == char:
                return False
            # 檢查所在的 3x3 九宮格是否已有重複
            # (row // 3) * 3 是該九宮格左上角的行座標
            # (col // 3) * 3 是該九宮格左上角的列座標
            box_row = 3 * (row // 3) + i // 3
            box_col = 3 * (col // 3) + i % 3
            if board[box_row][box_col] == char:
                return False
        return True
```

---
Source: notebooklm-source/0038-Count-and-Say.md

# 0038 - Count and Say (外觀數列)

## 1. 題目理解 (Problem Comprehension)

「外觀數列」是一個整數序列，其生成規則如下：
*   `countAndSay(1) = "1"`
*   `countAndSay(n)` 是對 `countAndSay(n-1)` 的描述，然後轉換成另一個字串。

**如何「描述」一個字串？**
將字串中相鄰且相同的數字進行分組，然後寫下每一組的「個數」和「數字」。
*   `"1"` -> 描述為「一個 1」，寫作 `"11"`。
*   `"11"` -> 描述為「兩個 1」，寫作 `"21"`。
*   `"21"` -> 描述為「一個 2，一個 1」，寫作 `"1211"`。
*   `"1211"` -> 描述為「一個 1，一個 2，兩個 1」，寫作 `"111221"`。

給你一個正整數 `n`，返回外觀數列的第 `n` 項。

**輸入與輸出格式：**
*   **輸入 (Input):** `n`: 正整數 (1 到 30)。
*   **輸出 (Output):** 第 `n` 項字串。

## 2. 思路分析 (Thought Process)

這道題的核心是實現一個「描述 (Say)」函式。我們可以按照題目給出的遞迴定義來處理，或者使用疊代法。

**優化思路：疊代與分組計數**
1.  **初始化**：從 `res = "1"` 開始。
2.  **循環 `n-1` 次**：每次都根據當前的 `res` 生成下一個字串。
3.  **生成下一個字串的方法**：
    *   使用一個指標 `i` 遍歷當前字串。
    *   計算與 `s[i]` 相同的連續字符數量 `count`。
    *   將 `str(count)` 和 `s[i]` 加入新字串。
    *   移動 `i` 到下一組不同的字符開始處。

## 3. 演算法設計 (Algorithm Design)

我們採用 **疊代模擬法**。

**偽代碼 (Pseudo-code):**

```text
Function countAndSay(n):
    res = "1"
    For k from 2 to n:
        res = describe(res)
    Return res

Function describe(s):
    next_s = ""
    i = 0
    While i < length(s):
        count = 1
        While i + 1 < length(s) and s[i] == s[i+1]:
            count++
            i++
        next_s = next_s + str(count) + s[i]
        i++
    Return next_s
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(M)**
    *   其中 M 是數列中所有字串的總長度。雖然難以給出精確的複雜度，但因為 `n` 最大隻到 30，且字串長度增長有限，這個方法非常高效。
*   **空間複雜度 (Space Complexity): O(M)**
    *   需要存儲生成的字串。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        # 1. 基礎情況：第一項是 "1"
        if n == 1:
            return "1"
            
        # 初始項
        res = "1"
        
        # 2. 透過迴圈，從第 1 項推導出第 n 項
        for _ in range(n - 1):
            res = self._get_next(res)
            
        return res
        
    def _get_next(self, s: str) -> str:
        # 輔助函式：根據「外觀」描述規則生成下一個字串
        next_s = [] # 使用列表存儲字串片段，最後再 join，效率比字串直接相加高
        i = 0
        
        while i < len(s):
            # 3. 找出相同字符的連續區塊
            count = 1
            # 只要下一個字符跟目前相同，就繼續增加計數
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            
            # 4. 根據規則，先寫下「個數」，再寫下「數字本身」
            next_s.append(str(count))
            next_s.append(s[i])
            
            # 移到下一個字符
            i += 1
            
        return "".join(next_s)
```

---
Source: notebooklm-source/0039-Combination-Sum.md

# 0039 - Combination Sum (組合總和)

## 1. 題目理解 (Problem Comprehension)

給你一個 **無重複元素** 的整數陣列 `candidates` 和一個目標整數 `target` ，找出 `candidates` 中可以使數字和為目標數 `target` 的所有 **不重複組合** 。

**關鍵規則：**
1.  `candidates` 中的數字可以 **無限制重複選擇**。
2.  組合中的數字順序不重要，只要數字出現的次數相同就被視為同一個組合。
3.  `target` 是一個正整數。

**輸入與輸出格式：**
*   **輸入 (Input):** `candidates`: 整數列表, `target`: 目標和。
*   **輸出 (Output):** 包含所有符合條件的子列表的列表。

**範例：**
輸入: `candidates = [2,3,6,7], target = 7`
輸出: `[[2,2,3],[7]]`

## 2. 思路分析 (Thought Process)

這是一個典型的搜尋空間問題，我們需要探索所有可能的數字組合。因為數字可以重複使用，且我們需要列出所有具體的組合，**回溯演算法 (Backtracking)** 是最合適的選擇。

**如何構建決策樹？**
在每一個步驟，我們都可以從 `candidates` 中選擇一個數字：
*   **選擇後**：`target` 減少。
*   **因為可以重複使用**：下一步我們依然可以從當前的數字開始選。
*   **為了避免重複組合**：我們只往後選，不回頭選之前的數字。

**優化：剪枝 (Pruning)**
如果我們對 `candidates` 進行**排序**，那麼當我們發現某個數字已經大於剩餘的 `target` 時，後面的數字肯定也大於 `target`，我們可以立即停止當前分支的搜尋。

## 3. 演算法設計 (Algorithm Design)

我們採用 **回溯法 + 剪枝**。

**偽代碼 (Pseudo-code):**

```text
Function combinationSum(candidates, target):
    Sort candidates
    res = []
    
    Function backtrack(remain, path, start_index):
        If remain == 0:
            Add path to res
            Return
            
        For i from start_index to length(candidates) - 1:
            # 剪枝
            If candidates[i] > remain: Break
            
            # 選擇
            path.push(candidates[i])
            # 遞迴，注意這裡還是傳 i，因為可以重複選
            backtrack(remain - candidates[i], path, i)
            # 撤銷
            path.pop()
            
    backtrack(target, [], 0)
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N^(T/M))**
    *   N 是候選數字量，T 是目標值，M 是候選中的最小數值。這是鬆散的上界，實際因為剪枝會快很多。
*   **空間複雜度 (Space Complexity): O(T/M)**
    *   主要是遞迴堆疊的深度。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 1. 先對陣列進行排序，這對於後面的「剪枝」優化至關重要
        candidates.sort()
        
        # 2. 定義回溯函式
        # remain: 還剩多少數額要湊齊
        # path: 目前已經選擇的數字組合
        # start_index: 從哪個位置開始選擇，避免回頭選導致重複組合
        def backtrack(remain, path, start_index):
            # 基礎情況：剛好湊齊
            if remain == 0:
                # 存入結果（記得要做一份複本，因為 path 在回溯中會變動）
                res.append(list(path))
                return
            
            # 3. 遍歷候選數字
            for i in range(start_index, len(candidates)):
                # [剪枝優化]
                # 因為 candidates 已經排序過，如果目前的數字已經大於餘額，
                # 後面更大的數字也絕對不可能湊齊，直接跳出迴圈
                if candidates[i] > remain:
                    break
                
                # 4. 做選擇：將數字加入目前的組合
                path.append(candidates[i])
                
                # 5. 遞迴搜尋：
                # 注意第二個參數依然傳入 i，而不是 i + 1
                # 因為題目允許「無限重複選擇」同一個數字
                backtrack(remain - candidates[i], path, i)
                
                # 6. 回溯：撤銷剛才的選擇，嘗試下一個數字
                path.pop()
                
        # 從第 0 個位置開始搜尋目標金額
        backtrack(target, [], 0)
        return res
```

---
Source: notebooklm-source/0040-Combination-Sum-II.md

# 0040 - Combination Sum II (組合總和 II)

## 1. 題目理解 (Problem Comprehension)

給你一個整數陣列 `candidates` 和一個目標數 `target` ，找出 `candidates` 中所有可以使數字和為 `target` 的組合。

**關鍵規則與變更：**
1.  `candidates` 中的每個數字在每個組合中 **只能使用一次** 。
2.  `candidates` 中可能包含 **重複的數字**（例如有兩個 `1`）。
3.  解集不能包含重複的組合。

這道題是 `0039 - Combination Sum` 的變體，差別在於處理重複元素的方式。

**輸入與輸出格式：**
*   **輸入 (Input):** `candidates`: 包含（可能有重複）數字的列表, `target`: 目標和。
*   **輸出 (Output):** 所有不重複的組合列表。

## 2. 思路分析 (Thought Process)

這題有兩個主要挑戰：
1.  **每個數字只能用一次**：這很簡單，在遞迴時將索引加 1 (`i + 1`) 即可。
2.  **避免結果中出現重複組合**：這是重點。如果 `candidates = [1, 1, 7]`，選第一個 `1` 和 `7` 得到 `[1, 7]`，選第二個 `1` 和 `7` 也會得到 `[1, 7]`。這就是重複。

**優化思路：排序 + 層級去重**
1.  **排序**：同樣先將 `candidates` 排序。
2.  **層級去重**：在遍歷當前層級的候選數字時，如果發現當前的數字跟前一個一樣（且前一個沒被選中），則跳過。
    *   這代表我們已經嘗試過以這個數值作為該位置的組合了。

## 3. 演算法設計 (Algorithm Design)

我們採用 **回溯法 + 同層去重**。

**偽代碼 (Pseudo-code):**

```text
Function combinationSum2(candidates, target):
    Sort candidates
    res = []
    
    Function backtrack(remain, path, start_index):
        If remain == 0:
            Add path to res
            Return
            
        For i from start_index to length(candidates) - 1:
            # 剪枝
            If candidates[i] > remain: Break
            
            # 同層去重：如果目前數字跟上一個一樣，跳過
            If i > start_index AND candidates[i] == candidates[i-1]:
                Continue
            
            # 選擇並遞迴（傳入 i + 1，表示不可重複選）
            path.push(candidates[i])
            backtrack(remain - candidates[i], path, i + 1)
            path.pop()
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(2^N * N)**
    *   在最壞情況下，每個數字都有選或不選兩種可能。
*   **空間複雜度 (Space Complexity): O(N)**
    *   遞迴深度最大為 N。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. 排序是處理重複元素的核心
        candidates.sort()
        res = []
        
        def backtrack(remain, path, start_index):
            # 基礎情況：湊齊目標值
            if remain == 0:
                res.append(list(path))
                return
            
            for i in range(start_index, len(candidates)):
                # [優化：剪枝] 
                # 剩下的數一定比 candidates[i] 大，所以不可能湊齊
                if candidates[i] > remain:
                    break
                
                # [關鍵：去重]
                # 如果當前數字與前一個數字相同，且前一個數字是在「同一層」被跳過的
                # 我們就不再重複嘗試這個數字，否則會產生重複的組合路徑
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                # 做選擇
                path.append(candidates[i])
                
                # 遞迴：傳入 i + 1
                # 因為同一個索引的數字不能重複使用
                backtrack(remain - candidates[i], path, i + 1)
                
                # 回溯
                path.pop()
                
        backtrack(target, [], 0)
        return res
```

---
Source: notebooklm-source/0041-First-Missing-Positive.md

# 0041 - First Missing Positive (缺失的第一個正數)

## 1. 題目理解 (Problem Comprehension)

給你一個未排序的整數陣列 `nums` ，請你找出其中沒有出現過的最小正整數。

**特別要求：**
*   時間複雜度必須為 **O(n)**。
*   空間複雜度必須為 **O(1)**。

這是一道 LeetCode 的 **Hard** 題目，難點在於如何在限制空間的情況下完成 O(n) 的搜尋。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 未排序的整數列表。
*   **輸出 (Output):** 最小的缺失正整數。

**範例：**
輸入: `[1, 2, 0]` -> 輸出: `3`
輸入: `[3, 4, -1, 1]` -> 輸出: `2`
輸入: `[7, 8, 9]` -> 輸出: `1`

## 2. 思路分析 (Thought Process)

既然空間限制在 O(1)，我們不能使用额外的 Hash Set。唯一的辦法就是 **原地利用輸入陣列本身**。

**關鍵觀察：**
對於一個長度為 `N` 的陣列，缺失的第一個正整數一定在 `[1, N+1]` 之間。
*   如果陣列剛好包含 `1, 2, ..., N`，答案就是 `N+1`。
*   否則，答案一定在 `1` 到 `N` 之間。

**優化思路：原地哈希 / 桶排序 (Cyclic Sort)**
我們可以嘗試把每個數字搬到它「應該在」的位置。
*   數字 `1` 應該放在 `nums[0]`。
*   數字 `2` 應該放在 `nums[1]`。
*   數字 `x` 應該放在 `nums[x-1]`。

**步驟：**
1.  遍歷陣列，如果當前數字 `x` 在 `[1, N]` 範圍內，且它不在正確位置 `nums[x-1]` 上，我們就把它與 `nums[x-1]` 位置上的數字交換。
2.  重複交換直到當前格子的數字正確，或者超出範圍，或者目標位置已經有正確數字（處理重複）。
3.  第二次遍歷陣列，找出第一個 `nums[i] != i + 1` 的位置，答案就是 `i + 1`。
4.  如果都符合，答案就是 `N + 1`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **原地哈希 (In-place Hashing)**。

**偽代碼 (Pseudo-code):**

```text
Function firstMissingPositive(nums):
    n = length(nums)
    
    For i from 0 to n - 1:
        # 當前數字 nums[i] 應該在索引 nums[i]-1
        While 1 <= nums[i] <= n AND nums[nums[i]-1] != nums[i]:
            Swap(nums[i], nums[nums[i]-1])
            
    For i from 0 to n - 1:
        If nums[i] != i + 1:
            Return i + 1
            
    Return n + 1
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   雖然有 `while` 迴圈，但每次交換都會把至少一個數字放到正確位置，所以總交換次數不會超過 N。
*   **空間複雜度 (Space Complexity): O(1)**
    *   直接修改原陣列。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 1. 桶排序思想：嘗試將數字 x 放到索引 x-1 的位置
        for i in range(n):
            # 只要當前數字在 [1, n] 之間，且它還沒被放在正確的位置上
            # 就持續進行交換
            # nums[nums[i]-1] != nums[i] 這一條能同時處理「位置錯誤」與「重複數字」
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                # 取得該數字應該去的索引
                correct_idx = nums[i] - 1
                
                # 交換目前位置與目標位置的數字
                # 這樣 nums[correct_idx] 就變成了 correct_idx + 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # 2. 第二次遍歷：尋找第一個「德不配位」的位置
        for i in range(n):
            # 如果索引 i 的位置存的不是 i + 1，說明 i + 1 就是缺失的最小正數
            if nums[i] != i + 1:
                return i + 1
                
        # 3. 如果 1 到 n 都整齊排列，則缺失的是下一個正數
        return n + 1
```

---
Source: notebooklm-source/0042-Trapping-Rain-Water.md

# 0042 - Trapping Rain Water (接雨水)

## 1. 題目理解 (Problem Comprehension)

給你一個非負整數陣列 `height` ，每個數代表一個寬度為 1 的柱子的高度。請計算雨天之後，這些柱子之間能接住多少雨水。

這是一道非常經典的 LeetCode **Hard** 題目。

**輸入與輸出格式：**
*   **輸入 (Input):** `height`: 整數列表。
*   **輸出 (Output):** 總接水量 (int)。

**範例：**
輸入: `[0,1,0,2,1,0,1,3,2,1,2,1]`
輸出: `6`

## 2. 思路分析 (Thought Process)

雨水是怎麼被接住的？對於每一個位置 `i`，它能接住的水取決於：
1.  它左邊最高的柱子 `left_max`。
2.  它右邊最高的柱子 `right_max`。
3.  它能接的水量 = `min(left_max, right_max) - height[i]`。

如果 `min(left_max, right_max)` 比當前高度還低，接水量就是 0。

### 直觀解法：動態規劃
預先算出每個位置對應的 `left_max` 陣列和 `right_max` 陣列。
*   時間複雜度：O(N)
*   空間複雜度：O(N) 用於存儲兩個陣列。

### 優化思路：雙指針 (Two Pointers)
我們可以用兩個指針 `left` 和 `right` 從兩端向中間移動。

**關鍵邏輯**：
如果 `height[left] < height[right]`，那麼對於 `left` 位置來說，雖然我們不知道右邊真正的 `right_max` 是多少，但我們知道它一定大於等於目前的 `height[right]`。
因此，`left` 位置能接的水只受限於 `left_max`。
只要 `left_max > height[left]`，就能接水。

同理，如果 `height[right] <= height[left]`，則 `right` 位置能接的水只受限於 `right_max`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **雙指針法**。

**偽代碼 (Pseudo-code):**

```text
Function trap(height):
    left = 0, right = length - 1
    left_max = 0, right_max = 0
    res = 0
    
    While left < right:
        If height[left] < height[right]:
            If height[left] >= left_max:
                left_max = height[left]
            Else:
                res += left_max - height[left]
            left++
        Else:
            If height[right] >= right_max:
                right_max = height[right]
            Else:
                res += right_max - height[right]
            right--
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   只需要遍歷一次陣列。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        # 初始化左右雙指針
        left, right = 0, len(height) - 1
        # 記錄左側遇到的最高柱子和右側遇到的最高柱子
        left_max, right_max = 0, 0
        res = 0
        
        while left < right:
            # 核心邏輯：木桶原理
            # 水量取決於較短的那一邊。
            # 如果左邊比右邊矮，那麼左邊能接的水只取決於左邊的最高點
            if height[left] < height[right]:
                if height[left] >= left_max:
                    # 如果當前高度更高，更新左側最高點，接不到水
                    left_max = height[left]
                else:
                    # 如果當前高度比左側最高點矮，差距就是能接的水量
                    res += left_max - height[left]
                # 移動左指針
                left += 1
            else:
                # 同理處理右邊
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                # 移動右指針
                right -= 1
                
        return res
```

---
Source: notebooklm-source/0043-Multiply-Strings.md

# 0043 - Multiply Strings (字串相乘)

## 1. 題目理解 (Problem Comprehension)

給你兩個以字串形式表示的非負整數 `num1` 和 `num2` ，返回 `num1` 和 `num2` 的乘積，也表示為字串形式。

**關鍵限制：**
*   不能使用任何內建的 BigInteger 函式庫。
*   **不能直接將輸入轉換為整數**（意指不能使用 `int(num1) * int(num2)` 這種偷懶做法）。

**輸入與輸出格式：**
*   **輸入 (Input):** `num1`, `num2`: 字串形式的整數。
*   **輸出 (Output):** 字串形式的乘積。

**範例：**
輸入: `num1 = "123", num2 = "456"`
輸出: `"56088"`

## 2. 思路分析 (Thought Process)

這道題要求我們模擬小學學過的「直式乘法」。

**關鍵觀察：**
1.  如果一個數字長度為 `M`，另一個長度為 `N`，它們乘積的長度最大為 `M + N`。
2.  在乘法中，`num1[i]` 與 `num2[j]` 相乘的結果，應該被加到結果陣列的第 `i + j` 個位置（如果從個位數算起）。

**優化思路：模擬手算乘法**
1.  建立一個長度為 `M + N` 的陣列 `res`，初始化為 0。
2.  將 `num1` 和 `num2` 反轉，方便從個位數開始計算（索引 0 對應個位）。
3.  兩層迴圈：遍歷 `num1` 的每一位 `i` 和 `num2` 的每一位 `j`：
    *   `mul = int(num1[i]) * int(num2[j])`
    *   將 `mul` 加到 `res[i + j]`。
    *   處理進位：將 `res[i+j] // 10` 加到 `res[i+j+1]`，並讓 `res[i+j]` 保持個位數。
4.  最後將 `res` 陣列反轉回來，移除多餘的前導 0，並拼接成字串。

## 3. 演算法設計 (Algorithm Design)

我們採用 **位置映射乘法模擬**。

**偽代碼 (Pseudo-code):**

```text
Function multiply(num1, num2):
    If num1 == "0" OR num2 == "0": Return "0"
    
    m, n = length(num1), length(num2)
    res = array of size m + n, initialized to 0
    
    # 從右往左遍歷
    For i from m - 1 down to 0:
        For j from n - 1 down to 0:
            mul = digit(num1[i]) * digit(num2[j])
            p1, p2 = i + j, i + j + 1
            
            sum = mul + res[p2]
            res[p2] = sum % 10
            res[p1] += sum / 10
            
    # 轉換為字串並處理開頭 0
    Return join(res)
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(M * N)**
    *   需要兩層迴圈遍歷兩個字串的所有位數組合。
*   **空間複雜度 (Space Complexity): O(M + N)**
    *   需要一個陣列來存儲每一位的結果。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 1. 處理特殊情況：任一數為 "0"，結果即為 "0"
        if num1 == "0" or num2 == "0":
            return "0"
            
        m, n = len(num1), len(num2)
        # 2. 乘積的最大長度為 m + n
        # 我們用列表來儲存每一位的計算結果（個位在後）
        res = [0] * (m + n)
        
        # 3. 為了方便從個位開始算，我們先把字串反轉
        # 這樣 num1[0] 就是個位，num1[1] 是十位，以此類推
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        # 4. 雙層迴圈模擬乘法
        for i in range(m):
            for j in range(n):
                # 計算當前兩位數字的乘積
                mul = int(num1[i]) * int(num2[j])
                
                # 關鍵：num1[i] 與 num2[j] 的乘積應該累加在 res[i+j] 位
                # 這裡 i+j 代表的是 10^(i+j) 的位數
                res[i + j] += mul
                
                # 5. 處理進位
                # 將多出的十位加到下一位
                res[i + j + 1] += res[i + j] // 10
                # 當前位只保留個位
                res[i + j] %= 10
                
        # 6. 移除計算過程中可能產生的前導 0（在列表末尾）
        # 但要保證至少留下一位（例如 0 * 0 的情況，雖然上面已處理）
        while len(res) > 1 and res[-1] == 0:
            res.pop()
            
        # 7. 將列表反轉回來（恢復正常順序），轉為字串並拼接
        # map(str, ...) 將 [5, 6, 0] 轉為 ['5', '6', '0']
        return "".join(map(str, res[::-1]))
```

---
Source: notebooklm-source/0044-Wildcard-Matching.md

# 0044 - Wildcard Matching (萬用字元匹配)

## 1. 題目理解 (Problem Comprehension)

給你一個輸入字串 `s` 和一個模式 `p` ，請你實現一個支持 `'?'` 和 `'*'` 的萬用字元匹配：

*   `'?'`：可以匹配任何**單個**字符。
*   `'*'`：可以匹配**任意序列**的字符（包括空序列）。
*   匹配必須覆蓋**整個**輸入字串。

這是一道 LeetCode 的 **Hard** 題目。

**輸入與輸出格式：**
*   **輸入 (Input):** `s`, `p`: 字串。
*   **輸出 (Output):** `True` 或 `False`。

**範例：**
1.  `s = "aa", p = "*"` -> `True`
2.  `s = "cb", p = "?a"` -> `False`
3.  `s = "adceb", p = "*a*b"` -> `True`

## 2. 思路分析 (Thought Process)

這道題跟 `0010 - Regular Expression Matching` 很像，但規則略有不同。這裡的 `*` 是獨立的萬用字元，可以代表任何長度的字串。

**優化思路：動態規劃 (Dynamic Programming)**
我們定義 `dp[i][j]` 表示 `s` 的前 `i` 個字符與 `p` 的前 `j` 個字符是否匹配。

**轉移方程：**
1.  **如果 `p[j-1] == '*'`**：
    *   **情況 A：`*` 匹配空字串**。那麼 `dp[i][j] = dp[i][j-1]` (無視這個 `*`)。
    *   **情況 B：`*` 匹配一個或多個字符**。那麼 `dp[i][j] = dp[i-1][j]` (保留這個 `*` 繼續匹配 `s` 的前一個位置)。
    *   結論：`dp[i][j] = dp[i][j-1] or dp[i-1][j]`。
2.  **如果 `p[j-1] == '?'` 或 `p[j-1] == s[i-1]`**：
    *   目前的字符匹配成功，取決於之前的結果。
    *   結論：`dp[i][j] = dp[i-1][j-1]`。
3.  **否則**：
    *   不匹配，`dp[i][j] = False`。

**基礎情況 (Base Case)：**
*   `dp[0][0] = True` (空字串與空模式匹配)。
*   `dp[0][j]`：如果模式前 `j` 個全是 `*`，則為 `True`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **二維動態規劃**。

**偽代碼 (Pseudo-code):**

```text
Function isMatch(s, p):
    m = length(s), n = length(p)
    dp = array [m+1][n+1] initialized to False
    dp[0][0] = True
    
    # 處理開頭的 *
    For j from 1 to n:
        If p[j-1] == '*': dp[0][j] = dp[0][j-1]
        Else: break
        
    For i from 1 to m:
        For j from 1 to n:
            If p[j-1] == '*':
                dp[i][j] = dp[i][j-1] OR dp[i-1][j]
            Else if p[j-1] == '?' OR p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
                
    Return dp[m][n]
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(M * N)**
    *   填滿一個 M*N 的表格。
*   **空間複雜度 (Space Complexity): O(M * N)**
    *   使用二維陣列（可優化至 O(N)）。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # 1. 建立 DP 表格，長度各加 1 用來代表「空字串」的情況
        # dp[i][j] 代表 s 的前 i 個字符與 p 的前 j 個字符是否匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # 2. 基礎情況：空對空是匹配的
        dp[0][0] = True
        
        # 3. 初始化第一行 (s 是空，p 有內容)
        # 只有當 p 全部由 '*' 組成時，才能匹配空字串 s
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
            else:
                # 只要遇到一個不是 '*' 的，後面就都不可能匹配空字串了
                break
                
        # 4. 開始填充表格
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 情況一：模式目前的字符是 '*'
                if p[j - 1] == '*':
                    # '*' 有兩種可能：
                    # dp[i][j-1]: '*' 匹配 0 個字符 (當作它不存在)
                    # dp[i-1][j]: '*' 匹配 1 個或多個字符 (消耗 s 的一個字符後，依然保留 p 的 '*')
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                
                # 情況二：模式目前的字符是 '?' 或者與 s 的字符剛好相等
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # 匹配成功，結果取決於「左上角」 (即 s 和 p 各少一個字符時的結果)
                    dp[i][j] = dp[i - 1][j - 1]
                    
                # 情況三：不匹配 (預設值就是 False，所以可以不寫)
                    
        return dp[m][n]
```

---
Source: notebooklm-source/0045-Jump-Game-II.md

# 0045 - Jump Game II (跳躍遊戲 II)

## 1. 題目理解 (Problem Comprehension)

給你一個非負整數陣列 `nums` ，你最初位於陣列的第一個位置。
陣列中的每個元素代表你在該位置可以跳躍的最大長度。

你的目標是使用 **最少的跳躍次數** 到達陣列的最後一個位置。
假設你總是可以用最少的跳躍次數到達。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 整數列表。
*   **輸出 (Output):** 最少跳躍次數 (int)。

**範例：**
輸入: `[2, 3, 1, 1, 4]`
輸出: `2`
（從索引 0 跳到索引 1，再從索引 1 跳到末尾）

## 2. 思路分析 (Thought Process)

這道題可以用動態規劃 (DP) 解，但時間複雜度會是 O(N^2)。
既然要求「最少步數」，且每次跳躍都有一個範圍，我們可以用 **貪心演算法 (Greedy Algorithm)** 來達到 O(N)。

**核心思想：**
每一跳都想著「下一步我最遠能跳到哪裡」。我們不需要在當前這步就決定具體跳到哪，而是觀察在**目前這一跳能覆蓋的範圍內**，哪一個點能讓我們**下一跳跳得最遠**。

**關鍵變數：**
1.  `jumps`: 跳躍次數。
2.  `current_jump_end`: 目前這一跳最遠能到達的邊界。
3.  `farthest`: 在 `current_jump_end` 範圍內，我們能跳到的下一個最遠點。

**步驟：**
1.  遍歷陣列（除了最後一個元素，因為到達最後一個元素就結束了）。
2.  更新 `farthest = max(farthest, i + nums[i])`。
3.  如果我們走到了目前這一跳的邊界 `current_jump_end`：
    *   必須再跳一次：`jumps++`。
    *   更新邊界為剛才找到的最遠點：`current_jump_end = farthest`。

## 3. 演算法設計 (Algorithm Design)

我們採用 **貪心演算法**。

**偽代碼 (Pseudo-code):**

```text
Function jump(nums):
    If length <= 1: Return 0
    
    jumps = 0
    current_end = 0
    farthest = 0
    
    For i from 0 to length - 2:
        farthest = max(farthest, i + nums[i])
        
        If i == current_end:
            jumps++
            current_end = farthest
            If current_end >= length - 1: Break
            
    Return jumps
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N)**
    *   只需要遍歷一次陣列。
*   **空間複雜度 (Space Complexity): O(1)**
    *   只使用了常數個變數。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # 1. 基礎情況：如果只有一個元素，不需要跳躍
        if len(nums) <= 1:
            return 0
            
        jumps = 0            # 跳躍次數
        current_jump_end = 0  # 目前這一跳能到達的最遠邊界
        farthest = 0         # 在目前範圍內，下一步最遠能跳到的位置
        
        # 2. 遍歷陣列，直到倒數第二個元素
        # 為什麼不包含最後一個？因為一旦 current_jump_end 覆蓋了最後一個，就完成了
        for i in range(len(nums) - 1):
            # 3. 不斷更新從目前能跳到的所有點出發，下一次最遠能到哪裡
            farthest = max(farthest, i + nums[i])
            
            # 4. 當我們走到了目前這一跳的盡頭
            if i == current_jump_end:
                # 必須增加一次跳躍次數
                jumps += 1
                # 將「新的邊界」設為剛才尋找到的最遠點
                current_jump_end = farthest
                
                # [優化] 如果新邊界已經可以到達終點，提早結束
                if current_jump_end >= len(nums) - 1:
                    break
                    
        return jumps
```

---
Source: notebooklm-source/0046-Permutations.md

# 0046 - Permutations (全排列)

## 1. 題目理解 (Problem Comprehension)

給你一個 **不含重複數字** 的陣列 `nums` ，返回其所有可能的全排列。你可以按 **任意順序** 返回答案。

**全排列**：是指將一個集合中的所有元素以各種可能的順序重新排列。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 包含唯一數字的列表。
*   **輸出 (Output):** 所有排列的列表 (List[List[int]])。

**範例：**
輸入: `[1, 2, 3]`
輸出: `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

## 2. 思路分析 (Thought Process)

這是一個典型的「決策樹」問題。對於每個位置，我們都從剩下的數字中挑選一個填進去。

**優化思路：回溯演算法 (Backtracking)**
1.  **選擇**：從候選數字中選一個。
2.  **遞迴**：繼續處理剩下的數字。
3.  **撤銷**：當走完一條路徑後，回到上一步，改選別的數字。

**具體操作：**
*   在遞迴函式中，傳入目前的 `path`（已選數字）和 `remaining_nums`（尚未選的數字）。
*   遍歷 `remaining_nums`，每次取出一格，加入 `path`，然後進入下一層。
*   當 `remaining_nums` 為空時，說明我們完成了一種全排列。

## 3. 演算法設計 (Algorithm Design)

我們採用 **回溯法**。

**偽代碼 (Pseudo-code):**

```text
Function permute(nums):
    res = []
    
    Function backtrack(current_nums, path):
        If current_nums is empty:
            Add path to res
            Return
            
        For i from 0 to length(current_nums) - 1:
            # 選擇第 i 個數，剩下其餘的數
            next_nums = current_nums[:i] + current_nums[i+1:]
            backtrack(next_nums, path + [current_nums[i]])
            
    backtrack(nums, [])
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N * N!)**
    *   總共有 N! 個排列，每個排列需要 O(N) 的時間來拷貝和生成。
*   **空間複雜度 (Space Complexity): O(N!)**
    *   用於儲存結果。遞迴深度為 N。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # 定義回溯函式
        # current_nums: 目前還剩下哪些數字可以挑選
        # path: 目前已經挑選並排好的數字序列
        def backtrack(current_nums, path):
            # 1. 終止條件：如果沒有數字可以挑選了
            # 代表目前這條路徑已經選滿了所有數字，是一個完整的排列
            if not current_nums:
                # 將目前的路徑存入結果
                res.append(path)
                return
            
            # 2. 遍歷目前所有可以挑選的數字
            for i in range(len(current_nums)):
                # 選擇第 i 個數字
                choice = current_nums[i]
                
                # 準備傳給下一層的剩餘數字 (排除掉剛選的這一個)
                remaining = current_nums[:i] + current_nums[i+1:]
                
                # 3. 進入遞迴：
                # 將新挑選的數字接到 path 後面，並傳入縮小後的剩餘數字列表
                backtrack(remaining, path + [choice])
                
                # 註：這裡之所以不用手動「撤銷」，是因為我們在呼叫時
                # 產生了新的列表 (path + [choice])，原本層級的變數並未被修改。
                
        # 從完整的 nums 和空的 path 開始搜尋
        backtrack(nums, [])
        return res
```

---
Source: notebooklm-source/0047-Permutations-II.md

# 0047 - Permutations II (全排列 II)

## 1. 題目理解 (Problem Comprehension)

給你一個可包含 **重複數字** 的序列 `nums` ，按 **任意順序** 返回所有不重複的全排列。

這道題是 `0046 - Permutations` 的變體，增加了「去重」的挑戰。

**輸入與輸出格式：**
*   **輸入 (Input):** `nums`: 可能包含重複數字的列表。
*   **輸出 (Output):** 所有不重複排列的列表。

**範例：**
輸入: `[1, 1, 2]`
輸出: `[[1,1,2], [1,2,1], [2,1,1]]`

## 2. 思路分析 (Thought Process)

如果在 `[1, 1, 2]` 中，我們像之前一樣處理，我們會把第一個 `1` 作為開頭生成排列，然後又把第二個 `1` 作為開頭生成同樣的排列。

**優化思路：排序 + 層級去重**
要避免生成重複的排列，最有效的方法是：
1.  **排序**：先將 `nums` 由小到大排序，讓相同的數字排在一起。
2.  **層級去重**：在每一層遞迴中，如果當前的數字與前一個數字相同（`nums[i] == nums[i-1]`），則直接跳過。
    *   這代表我們在「這個位置」上已經嘗試過這個數值了，不需要再次嘗試。

## 3. 演算法設計 (Algorithm Design)

我們採用 **回溯法 + 同層去重**。

**偽代碼 (Pseudo-code):**

```text
Function permuteUnique(nums):
    Sort nums
    res = []
    
    Function backtrack(current_nums, path):
        If current_nums is empty:
            Add path to res
            Return
            
        For i from 0 to length(current_nums) - 1:
            # 去重：如果跟前一個數字一樣，跳過
            If i > 0 AND current_nums[i] == current_nums[i-1]:
                Continue
            
            remaining = current_nums[:i] + current_nums[i+1:]
            backtrack(remaining, path + [current_nums[i]])
            
    backtrack(nums, [])
    Return res
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N * N!)**
    *   排列的數量級別。
*   **空間複雜度 (Space Complexity): O(N!)**
    *   結果集的大小。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 1. 排序是去重的關鍵
        # 排序後相同的數字會相鄰，我們就可以輕易判斷是否重複
        nums.sort()
        res = []
        
        # 定義回溯函式
        # current_nums: 當前層級還剩下哪些數字可以選
        # path: 目前已經選好的排列部分
        def backtrack(current_nums, path):
            # 2. 終止條件：數字選完了
            if not current_nums:
                res.append(path)
                return
            
            # 3. 遍歷候選數字
            for i in range(len(current_nums)):
                # [關鍵：去重邏輯]
                # 如果目前的數字跟前一個數字相同
                # 因為我們是從左往右選，如果前一個相同的數字剛被「選過」並回溯回來，
                # 我們就不應該在「同一個位置」再次選擇相同的數字。
                if i > 0 and current_nums[i] == current_nums[i - 1]:
                    continue
                
                # 4. 遞迴搜尋
                # 傳入排除掉目前選擇後的剩餘列表
                backtrack(current_nums[:i] + current_nums[i+1:], path + [current_nums[i]])
                
        # 從完整的 nums 開始搜尋
        backtrack(nums, [])
        return res
```

---
Source: notebooklm-source/0048-Rotate-Image.md

# 0048 - Rotate Image (旋轉圖像)

## 1. 題目理解 (Problem Comprehension)

給你一個 `n x n` 的二維矩陣 `matrix` 表示一個圖像。請你將圖像順時針旋轉 90 度。

**關鍵要求：**
*   你必須在 **原地 (In-place)** 修改輸入矩陣。
*   不能使用另一個矩陣來輔助旋轉。

**輸入與輸出格式：**
*   **輸入 (Input):** `matrix`: 二維整數列表。
*   **輸出 (Output):** 無（直接修改 `matrix`）。

**範例：**
輸入:
```text
[[1,2,3],
 [4,5,6],
 [7,8,9]]
```
輸出:
```text
[[7,4,1],
 [8,5,2],
 [9,6,3]]
```

## 2. 思路分析 (Thought Process)

直接進行 90 度旋轉的座標轉換可能有點燒腦。我們可以把這個複雜的變換拆解成兩個簡單的幾何操作。

**優化思路：轉置 + 左右翻轉 (Transpose + Reverse)**
觀察 90 度旋轉後的規律：
1.  **原本的第 0 行** 變成了 **旋轉後的最後一列**。
2.  **原本的最後一行** 變成了 **旋轉後的第 0 列**。

這可以透過以下兩步實現：
1.  **轉置 (Transpose)**：沿著主對角線（左上到右下）翻轉矩陣。
    *   將 `matrix[i][j]` 與 `matrix[j][i]` 對調。
    *   結果：原本的行變成了列（例如第 0 行變成第 0 列）。
2.  **左右翻轉 (Reverse rows)**：將每一行進行反轉。
    *   結果：原本的第 0 列變成最後一列，原本的最後一列變成第 0 列。

這兩步結合起來，剛好就是順時針旋轉 90 度！

## 3. 演算法設計 (Algorithm Design)

我們採用 **轉置並反轉行** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function rotate(matrix):
    n = length(matrix)
    
    # 1. 轉置
    For i from 0 to n - 1:
        For j from i + 1 to n - 1:
            Swap matrix[i][j] AND matrix[j][i]
            
    # 2. 左右翻轉每一行
    For i from 0 to n - 1:
        Reverse(matrix[i])
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N^2)**
    *   N 是矩陣的邊長。我們遍歷了矩陣兩次。
*   **空間複雜度 (Space Complexity): O(1)**
    *   直接在原矩陣上進行交換操作。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # 1. 第一步：矩陣轉置 (Transpose)
        # 將 matrix[i][j] 與 matrix[j][i] 交換
        # 注意內層迴圈從 i + 1 開始，避免重複交換回原位
        for i in range(n):
            for j in range(i + 1, n):
                # 交換對稱位置的元素
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # 2. 第二步：將每一行反轉 (Reverse)
        # 轉置後，原本的行已經變成了列，
        # 左右翻轉每一行，就達到了順時針旋轉 90 度的效果
        for i in range(n):
            # Python 內建的 reverse() 是原地操作，符合 O(1) 空間要求
            matrix[i].reverse()
```

---
Source: notebooklm-source/0049-Group-Anagrams.md

# 0049 - Group Anagrams (字母異位詞分組)

## 1. 題目理解 (Problem Comprehension)

給你一個字串陣列 `strs` ，請你將 **字母異位詞 (Anagrams)** 組合在一起。可以按任意順序返回結果列表。

**字母異位詞** 是指由同樣的字母組成的不同單詞。換句話說，如果兩個單詞包含的字母及其頻率都完全相同，只是順序不同，它們就是字母異位詞。

**輸入與輸出格式：**
*   **輸入 (Input):** `strs`: 字串列表。
*   **輸出 (Output):** 字串列表的列表 (List[List[str]])。

**範例：**
輸入: `["eat", "tea", "tan", "ate", "nat", "bat"]`
輸出: `[["bat"],["nat","tan"],["ate","eat","tea"]]`

## 2. 思路分析 (Thought Process)

問題在於：**如何判斷兩個字串是字母異位詞，並快速將它們歸類？**

如果兩個字串是字母異位詞，它們一定有一個共同的「特徵」。

**方法一：排序後作為鍵 (Sorting)**
字母異位詞排序後的結果是完全一樣的。
*   `"eat"` -> 排序為 `"aet"`
*   `"tea"` -> 排序為 `"aet"`
*   `"ate"` -> 排序為 `"aet"`
這就是我們要的共同特徵。我們可以用一個雜湊表 (Dictionary) 來儲存：
*   鍵 (Key): 排序後的字串。
*   值 (Value): 屬於該類別的原始字串列表。

**方法二：字元計數作為鍵 (Counting)**
如果不排序，也可以統計每個字母出現的次數（a-z 總共 26 個）。將這 26 個次數組成一個元組 (tuple) 作為鍵。這在某些情況下會更快，但方法一在 Python 中實作最簡潔。

## 3. 演算法設計 (Algorithm Design)

我們採用 **排序 + 雜湊表** 的方法。

**偽代碼 (Pseudo-code):**

```text
Function groupAnagrams(strs):
    Initialize map = empty dictionary
    
    For each s in strs:
        # 將字串排序，作為特徵鍵
        key = join(sort(s))
        
        If key not in map:
            map[key] = [s]
        Else:
            map[key].append(s)
            
    Return list of all values in map
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(N * K log K)**
    *   N 是字串個數，K 是單個字串的最大長度。每個字串都需要進行一次排序。
*   **空間複雜度 (Space Complexity): O(N * K)**
    *   需要雜湊表來存儲所有的字串。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. 建立一個字典，用來存放分組後的結果
        # 使用 defaultdict(list) 的好處是：當鍵不存在時，會自動建立一個空列表
        anagram_map = defaultdict(list)
        
        # 2. 遍歷輸入的每一個字串
        for s in strs:
            # 3. 核心邏輯：將字串中的字母進行排序
            # 例如 "eat" -> ['a', 'e', 't'] -> "aet"
            # 只要是字母組成相同的單詞，排序後的字串一定是一模一樣的
            sorted_s = "".join(sorted(s))
            
            # 4. 將原始字串加入對應特徵鍵的列表中
            anagram_map[sorted_s].append(s)
            
        # 5. 返回字典中所有的值（即所有的分組列表）
        return list(anagram_map.values())
```

---
Source: notebooklm-source/0050-Pow-x-n.md

# 0050 - Pow(x, n) (x 的 n 次冪)

## 1. 題目理解 (Problem Comprehension)

實現 `pow(x, n)` ，即計算 `x` 的 `n` 次冪函數（即 x^n）。

**輸入與輸出格式：**
*   **輸入 (Input):** `x`: 浮點數 (float), `n`: 整數 (int)。
*   **輸出 (Output):** `x^n` 的結果 (float)。

**範例：**
輸入: `x = 2.00000, n = 10` -> 輸出: `1024.00000`
輸入: `x = 2.00000, n = -2` -> 輸出: `0.25000`

## 2. 思路分析 (Thought Process)

最直覺的方法是將 `x` 連乘 `n` 次。
*   如果 `n = 10^9`，連乘 10 億次會太慢 (O(N))。
*   我們需要一種更高效的方法。

**優化思路：快速冪演算法 (Fast Power / Binary Exponentiation)**
利用「分治法」的思想：
*   如果我要算 `x^10`，我可以先算出 `x^5`，然後再把結果平方：`x^10 = (x^5)^2`。
*   如果我要算 `x^5`，我可以先算出 `x^2`，然後：`x^5 = x * (x^2)^2`。

這樣，我們每次都能將指數減少一半，計算次數會從 O(N) 降低到 **O(log N)**。

**處理負指數：**
*   根據數學規則：`x^(-n) = (1/x)^n`。
*   我們可以先將 `x` 變為 `1/x`，並將 `n` 變為正數，然後套用同樣的快速冪邏輯。

## 3. 演算法設計 (Algorithm Design)

我們採用 **遞迴式的快速冪**。

**偽代碼 (Pseudo-code):**

```text
Function myPow(x, n):
    If n == 0: Return 1
    If n < 0:
        x = 1 / x
        n = -n
        
    Function fast_pow(x, n):
        If n == 0: Return 1
        
        half = fast_pow(x, n / 2)
        
        If n is even:
            Return half * half
        Else:
            Return half * half * x
            
    Return fast_pow(x, n)
```

**複雜度分析：**

*   **時間複雜度 (Time Complexity): O(log N)**
    *   每次遞迴指數都減半。
*   **空間複雜度 (Space Complexity): O(log N)**
    *   遞迴堆疊的深度。

## 4. 程式碼實現與註解 (Code Implementation with Comments)

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1. 基礎情況：任何數的 0 次方都是 1
        if n == 0:
            return 1.0
            
        # 2. 處理負指數情況
        # x^(-n) 等於 (1/x) 的 n 次方
        if n < 0:
            x = 1 / x
            n = -n
            
        # 3. 定義快速冪的輔助遞迴函式
        def fast_pow(base, exp):
            # 遞迴終止條件
            if exp == 0:
                return 1.0
            
            # 核心：先算出指數一半的結果
            # 這樣我們只需要算一次，然後平方它即可
            half = fast_pow(base, exp // 2)
            
            # 如果指數是偶數，例如 x^10 = (x^5) * (x^5)
            if exp % 2 == 0:
                return half * half
            # 如果指數是奇數，例如 x^11 = (x^5) * (x^5) * x
            else:
                return half * half * base
                
        # 開始執行快速冪計算
        return fast_pow(x, n)
```

