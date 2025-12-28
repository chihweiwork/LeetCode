from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # We use the array itself as a hash table.
        # Ideally, nums[i] should store the value i + 1.
        for i in range(n):
            # While the current number is in the range [1, n]
            # and it's not at its correct position (nums[nums[i]-1])
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                # Swap it to its correct position
                # Using a temporary variable to avoid common Python swap pitfalls with list indexing
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Second pass: find the first index where the value is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # If all positions are correct, the missing number is n + 1
        return n + 1
