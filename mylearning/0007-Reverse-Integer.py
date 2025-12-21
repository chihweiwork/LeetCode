class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        positive = x > 0
        if not positive:
            x = x * -1

        while x!=0:
            y = x % 10
            x = x // 10

            result = result* 10 + y
        
        if result >= 2**31 -1 or result < -2**31:
            return 0 
        
        if not positive:
            return -1 * result
        
        return result
