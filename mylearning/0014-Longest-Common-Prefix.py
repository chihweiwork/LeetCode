from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Vertical Scanning
        # Iterate through each character of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Check this character against all other strings
            for j in range(1, len(strs)):
                # If we've reached the end of another string, or the characters don't match
                if i == len(strs[j]) or strs[j][i] != char:
                    # Return the prefix found so far
                    return strs[0][:i]
                    
        return strs[0]