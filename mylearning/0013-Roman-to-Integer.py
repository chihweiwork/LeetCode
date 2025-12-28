
class Solution:
  def romanToInt(self, s: str) -> int:
    """
    Converts a roman numeral to an integer.

    The key is to handle the subtractive cases (e.g., 'IV', 'IX').
    We can iterate through the string and if a character's value is
    less than the next character's value, we subtract it. Otherwise, add it.
    """
    
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    i = 0
    
    while i < len(s):
      # Check for subtractive case: current value is smaller than next value
      # and we are not at the end of the string.
      if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
        # This is a subtractive case, e.g., 'IV' (I < V)
        # Add the difference (e.g., 5 - 1 = 4)
        total += roman_map[s[i+1]] - roman_map[s[i]]
        # Move pointer two steps forward
        i += 2
      else:
        # This is an additive case, e.g., 'VI' (V > I)
        # Just add the current value
        total += roman_map[s[i]]
        # Move pointer one step forward
        i += 1
        
    return total
