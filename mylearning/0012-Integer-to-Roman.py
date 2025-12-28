
class Solution:
  def intToRoman(self, num: int) -> str:
    """
    Converts an integer to a roman numeral.

    This is solved using a greedy approach. We predefine the symbol values
    from largest to smallest, including the special subtractive cases
    (like 900 for 'CM', 400 for 'CD', etc.).
    """
    
    # The list must be ordered from largest to smallest value.
    value_symbols = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    
    roman_numeral = []
    
    # Greedily subtract the largest possible values from the number.
    for val, symbol in value_symbols:
      # While the number is large enough to subtract the current value
      while num >= val:
        # Append the corresponding symbol
        roman_numeral.append(symbol)
        # Subtract the value from the number
        num -= val
        
    return "".join(roman_numeral)

