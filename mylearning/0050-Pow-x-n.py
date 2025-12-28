class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: anything to the power 0 is 1
        if n == 0:
            return 1.0
            
        # Handle negative power: x^(-n) = (1/x)^n
        if n < 0:
            x = 1 / x
            n = -n
            
        # Fast Power Algorithm (Binary Exponentiation)
        # Using recursion:
        # x^n = (x^2)^(n/2) if n is even
        # x^n = x * (x^2)^(n/2) if n is odd
        def fast_pow(base, exp):
            if exp == 0:
                return 1.0
            half = fast_pow(base, exp // 2)
            if exp % 2 == 0:
                return half * half
            else:
                return half * half * base
                
        return fast_pow(x, n)
