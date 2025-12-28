class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] will be True if s[i:] matches p[j:]
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Empty string matches empty pattern
        dp[len(s)][len(p)] = True
        
        # Iterate from the end of both strings to the beginning
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                # Check if the first character matches
                first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
                
                # If there's a '*' coming up next
                if j + 1 < len(p) and p[j+1] == '*':
                    # Two cases for '*':
                    # 1. '*' matches 0 of the preceding element: dp[i][j+2]
                    # 2. '*' matches 1 or more: first_match and dp[i+1][j]
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    # Normal character match
                    dp[i][j] = first_match and dp[i+1][j+1]
                    
        return dp[0][0]
