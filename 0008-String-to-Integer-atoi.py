# https://leetcode.com/problems/string-to-integer-atoi/
#
# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
#
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0

        sign = 1
        i = 0
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            sign = -1
            i += 1

        num = 0
        while i < len(str) and str[i].isdigit():
            num = num * 10 + int(str[i])
            i += 1

        num *= sign

        if num > 2**31 - 1:
            return 2**31 - 1
        if num < -2**31:
            return -2**31
        
        return num
