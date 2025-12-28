from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(current_nums, path):
            # Base case: if no numbers left to pick, add current path to results
            if not current_nums:
                res.append(path)
                return
            
            # Iterate through the available numbers
            for i in range(len(current_nums)):
                # Choose the i-th number and recurse with the remaining numbers
                backtrack(current_nums[:i] + current_nums[i+1:], path + [current_nums[i]])
                
        backtrack(nums, [])
        return res
