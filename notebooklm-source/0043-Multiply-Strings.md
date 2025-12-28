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
