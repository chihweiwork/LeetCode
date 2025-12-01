# 0050. Pow x n

```python
# https://leetcode.com/problems/powx-n/
#
# Implement pow(x, n), which calculates x raised to the power n (xn).
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 0:
            return self.myPow(x*x, n//2)
        return x * self.myPow(x*x, (n-1)//2)

```