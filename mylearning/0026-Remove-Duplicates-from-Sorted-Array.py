from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # left is the pointer for the last unique element found
        left = 0
        
        # right is the scanning pointer
        for right in range(1, len(nums)):
            # If we found a new unique element
            if nums[right] != nums[left]:
                left += 1
                # Move the unique element to the front
                nums[left] = nums[right]
                
        # The length of unique elements is left + 1
        return left + 1
