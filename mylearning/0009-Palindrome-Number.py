class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes.
        # Also, if the last digit of the number is 0, then the first digit
        # must also be 0, which only happens if the number is 0.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + (x % 10)
            x //= 10
            
        # When the length is an odd number, we can get rid of the middle digit by reversed_half // 10
        # For example, for 121, at the end of the while loop we have x = 1, reversed_half = 12,
        # so since middle digit doesn't matter in palindrome(it will always equal to itself),
        # we can simply get rid of it.
        return x == reversed_half or x == reversed_half // 10