from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # Initialize result with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicates to optimize
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we found the exact target, return immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
