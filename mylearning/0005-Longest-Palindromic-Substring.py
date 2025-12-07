class Solution:

    def expand(self, left: int, right: int):

        valid_left, valid_right = left, right
        # 檢查長度
        while left >= 0 and right < len(self.target) and self.target[left] == self.target[right]:
            valid_left, valid_right = left, right
            left -= 1
            right += 1

        if valid_left == left and valid_right == right:
            return valid_left, valid_left
        else:
            return valid_left, valid_right
            

    def longestPalindrome(self, s: str) -> str:

        self.target = s
        max_length = 0
        result = ""

        for center in range(len(s)):

            left, right = self.expand(center, center) # odd
            if (right - left + 1) > max_length:
                result = self.target[left:right+1]
                max_length = len(result)

            left, right = self.expand(center, center+1) # event
            if (right - left + 1) > max_length:
                result = self.target[left:right+1]
                max_length = len(result)

        return result
        
