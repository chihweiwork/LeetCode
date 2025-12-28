class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is an empty string, return 0 (as per problem definition)
        if not needle:
            return 0
            
        n = len(haystack)
        m = len(needle)
        
        # Only need to iterate up to the point where needle can still fit
        for i in range(n - m + 1):
            # Check if the substring starting at i matches needle
            if haystack[i:i+m] == needle:
                return i
                
        return -1
