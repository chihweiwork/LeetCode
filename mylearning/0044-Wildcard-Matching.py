class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] is True if s[0...i-1] matches p[0...j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Handle cases where pattern starts with '*'
        # '*' can match an empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
            else:
                # Once we hit a non-'*' character, 
                # dp[0][j] and all subsequent will be False
                break
                
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Two sub-cases for '*':
                    # 1. '*' matches nothing: dp[i][j-1]
                    # 2. '*' matches at least one character: dp[i-1][j]
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # Current characters match or '?' used as wildcard
                    dp[i][j] = dp[i - 1][j - 1]
                    
        return dp[m][n]
