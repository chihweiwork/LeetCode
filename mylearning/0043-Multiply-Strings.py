class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
            
        m, n = len(num1), len(num2)
        # The product of a length m number and a length n number 
        # has at most m + n digits.
        res = [0] * (m + n)
        
        # Reverse the strings to work from least significant digit
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i in range(m):
            for j in range(n):
                # Multiply digit by digit
                mul = int(num1[i]) * int(num2[j])
                
                # The product adds to index i+j and possibly i+j+1 (carry)
                res[i + j] += mul
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
                
        # Remove trailing zeros (from the end of our list, which is the start of the number)
        # and convert back to string
        while len(res) > 1 and res[-1] == 0:
            res.pop()
            
        return "".join(map(str, res[::-1]))
