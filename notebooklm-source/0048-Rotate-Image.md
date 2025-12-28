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
