from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Two pointer approach: start from both ends
        left, right = 0, len(nums)
        
        while left < right:
            if nums[left] == val:
                # If current element is val, swap it with the last element
                # and decrease the size (right boundary)
                nums[left] = nums[right - 1]
                right -= 1
            else:
                # If it's not val, move to the next element
                left += 1
                
        return right
