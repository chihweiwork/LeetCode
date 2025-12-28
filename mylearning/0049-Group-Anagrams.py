from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a dictionary to store lists of strings
        # The key will be the sorted version of the string
        # Defaultdict avoids checking if key exists
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Anagrams will have the same sorted representation
            # e.g., "eat" -> "aet", "tea" -> "aet"
            key = "".join(sorted(s))
            anagram_map[key].append(s)
            
        # Return all the groups as a list of lists
        return list(anagram_map.values())
