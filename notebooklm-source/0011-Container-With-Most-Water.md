# LeetCode #11 - Container With Most Water (盛最多水的容器) 教學

嗨，同學！今天我們要挑戰的是 LeetCode 第 11 題，這是一個非常經典的面試題，它考察的是我們如何從暴力解法優化到更高效的演算法。

## 1. 題目理解

題目給我們一個陣列 `height`，每個數字代表一個垂直線的高度。我們要找出兩條線，讓它們和 x 軸一起構成一個容器，這個容器能裝的水要最多。

水量是怎麼計算的呢？想像一下木桶原理，一個木桶能裝多少水，取決於最短的那塊木板。同樣地，我們這個容器的容量由「**較短那條線的高度**」和「**兩條線之間的寬度**」決定。

**容量 (Area) = `min(height[i], height[j]) * (j - i)`**

我們的目標就是找到一對 `i` 和 `j`，讓這個容量最大化。

## 2. 思考過程 & 演算法選擇

### 方法一：暴力解法 (Brute Force)

最直覺的想法是什麼？就是把所有可能的組合都試一遍！

我們可以這樣做：
-   用一個迴圈 `i` 從頭開始遍歷。
-   在 `i` 迴圈裡面，再用一個迴圈 `j` 從 `i+1` 開始遍歷。
-   這樣我們就得到了所有 `(i, j)` 的組合，計算每一種組合的容量，然後用一個變數 `max_area` 來記錄最大的那個。

這個方法可行嗎？可行。但是效率好嗎？
假設 `height` 陣列的長度是 `n`，外層迴圈跑 `n` 次，內層迴圈平均也跑 `n/2` 次，所以時間複雜度是 **O(n²)**。當 `n` 很大的時候（例如 50000），`n²` 就是一個天文數字了，程式會跑非常久，在 LeetCode 上會「超時」(Time Limit Exceeded)。

所以，我們需要一個更聰明的演算法。

### 方法二：雙指針法 (Two-Pointer Technique)

這就是這題的精髓了！讓我們換個角度思考。

容器的寬度取決於兩條線的距離。想要寬度最大，那一開始兩條線就應該在**最兩端**，對吧？

所以，我們設定兩個指針 (pointer)：
-   `left` 指針，指向陣列的開頭 `0`。
-   `right` 指針，指向陣列的結尾 `len(height) - 1`。

這時候，我們的寬度 `width = right - left` 是最大的。我們計算一下這個初始狀態的容量。

接下來，我們要**移動其中一個指針**，來尋找有沒有可能出現更大的容量。問題來了，該移動 `left` 還是 `right` 呢？

讓我們來分析一下：
-   容器的高度取決於 `min(height[left], height[right])`。
-   現在，假設 `height[left]` 比較矮。
-   如果我們移動 `right` 指針（比較高的那個）往內縮，新的寬度 `width` 肯定會變小。而新的高度呢？因為還是受限於 `height[left]` 這個矮板，所以新的高度**最多**只會和現在一樣高，甚至可能更矮。寬度變小，高度不變或變小，那麼總容量**絕對不可能變大**。
-   反過來，如果我們移動 `left` 指針（比較矮的那個）往內縮，雖然寬度 `width` 也變小了，但新的 `height[left]` **有可能會變高**，高到足以彌補寬度的損失，從而讓總容量變得更大。

**結論：** 在每一步，我們都應該**移動指向較短線段的那個指針**。這是雙指針法的核心策略，因為只有這樣才有可能找到更大的容量。

演算法步驟：
1.  初始化 `left = 0`, `right = len(height) - 1`, `max_area = 0`。
2.  當 `left < right` 時，進入迴圈：
    a. 計算當前容量 `current_area`。
    b. 更新 `max_area = max(max_area, current_area)`。
    c. 比較 `height[left]` 和 `height[right]`，移動較短線段的那個指針。
3.  迴圈結束後，`max_area` 就是答案。

這個方法只需要從兩端向中間遍歷一次，時間複雜度是 **O(n)**，非常高效！

## 3. 程式碼實現

這是在 `mylearning/0011-Container-With-Most-Water.py` 中的解答：

```python
from typing import List

class Solution:
  def maxArea(self, height: List[int]) -> int:
    max_area = 0
    left, right = 0, len(height) - 1

    while left < right:
      # 容量由短板和寬度決定
      h = min(height[left], height[right])
      w = right - left
      current_area = h * w
      max_area = max(max_area, current_area)

      # 關鍵：移動指向短板的那個指針
      # 因為移動長板，寬度變小，高度受限於短板，面積一定不會變大
      # 移動短板，雖然寬度變小，但 h 有可能變大，面積才有可能變大
      if height[left] < height[right]:
        left += 1
      else:
        right -= 1
        
    return max_area
```

希望透過這個講解，你能掌握雙指針法的巧妙之處！這是一個在很多題目中都非常有用的技巧。
