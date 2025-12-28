from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Sort to easily identify duplicates
        nums.sort()
        res = []
        
        def backtrack(current_nums, path):
            if not current_nums:
                res.append(path)
                return
            
            for i in range(len(current_nums)):
                # Skip duplicate elements at the same level
                # This ensures we don't start a permutation with the same value twice
                if i > 0 and current_nums[i] == current_nums[i - 1]:
                    continue
                
                backtrack(current_nums[:i] + current_nums[i+1:], path + [current_nums[i]])
                
        backtrack(nums, [])
        return res
