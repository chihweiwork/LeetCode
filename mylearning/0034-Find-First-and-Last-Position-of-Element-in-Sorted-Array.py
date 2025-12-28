from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function to find the bound (left or right)
        def findBound(is_left: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if is_left:
                        # Continue searching in the left half to find the first position
                        right = mid - 1
                    else:
                        # Continue searching in the right half to find the last position
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return bound
            
        start = findBound(True)
        end = findBound(False)
        
        return [start, end]
