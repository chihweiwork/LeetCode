class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer range
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        # Handle overflow case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
            
        # Determine the sign of the result
        # True if they have the same sign, False otherwise
        is_positive = (dividend > 0) == (divisor > 0)
        
        a, b = abs(dividend), abs(divisor)
        res = 0
        
        # We use bit manipulation to simulate division
        # Instead of subtracting b from a one by one (O(a/b)),
        # we subtract powers of 2 times b (O(log(a/b))).
        while a >= b:
            temp_b, count = b, 1
            # Double temp_b until it's just about to exceed a
            while a >= (temp_b << 1):
                temp_b <<= 1
                count <<= 1
                
            # Subtract the largest possible multiple of b
            a -= temp_b
            res += count
            
        res = res if is_positive else -res
        
        # Ensure result is within 32-bit integer range
        return min(max(MIN_INT, res), MAX_INT)
