
class Solution:
  def isPalindrome(self, x: int) -> bool:
    """
    Checks if an integer is a palindrome.

    A palindrome is a number that reads the same backward as forward.
    Negative numbers are not considered palindromes.
    """
    # According to the problem, negative numbers are not palindromes.
    # Also, if a number ends in 0 and is not 0 itself, it cannot be a palindrome
    # (e.g., 10, 120).
    if x < 0 or (x % 10 == 0 and x != 0):
      return False

    # The most Pythonic and straightforward way is to convert the number
    # to a string and check if the string is equal to its reverse.
    s = str(x)
    return s == s[::-1]
