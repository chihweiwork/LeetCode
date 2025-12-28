from typing import List

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    """
    Finds the longest common prefix string amongst an array of strings.

    A clever and Pythonic approach is to sort the array of strings.
    The longest common prefix of all strings will be the common prefix
    of the lexicographically first and last strings in the sorted array.
    """
    if not strs:
      return ""
      
    # Sort the list of strings.
    # e.g., ["flower", "flow", "flight"] -> ["flight", "flow", "flower"]
    strs.sort()
    
    # The first and last strings in the sorted list will be the most different.
    # Any common prefix must be shared between them.
    first_str = strs[0]
    last_str = strs[-1]
    
    common_prefix = []
    
    # Iterate up to the length of the shorter of the two strings.
    for i in range(min(len(first_str), len(last_str))):
      if first_str[i] == last_str[i]:
        common_prefix.append(first_str[i])
      else:
        # Stop as soon as a character doesn't match.
        break
        
    return "".join(common_prefix)
