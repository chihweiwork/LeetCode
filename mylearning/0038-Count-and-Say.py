class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
            
        # Start with the first term
        res = "1"
        
        # Iteratively generate the next term n-1 times
        for _ in range(n - 1):
            res = self._get_next(res)
            
        return res
        
    def _get_next(self, s: str) -> str:
        # Helper function to generate the "saying" of string s
        next_s = []
        i = 0
        while i < len(s):
            count = 1
            # Count consecutive identical digits
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            
            # Add (count, digit) to our next string
            next_s.append(str(count))
            next_s.append(s[i])
            i += 1
            
        return "".join(next_s)
