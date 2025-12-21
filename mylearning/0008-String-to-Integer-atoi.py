class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        s = s[i:]
        sign = 1
        if not s: 
            return 0
        if s[0] == '+' or s[0] == '-':
            if s[0] == '-':
                sign = -1
            s = s[1:]
        
        i = 0
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + (ord(s[i]) - ord('0'))
            i += 1

        MAX = 2**31 - 1
        MIN = -2**31
        result = result * sign
        if result > MAX:
            return MAX
        elif result < MIN:
            return MIN
        else:
            return result
