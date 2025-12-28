from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Sorting helps in pruning the recursion tree
        candidates.sort()
        
        def backtrack(remain, stack, start_index):
            if remain == 0:
                # Found a valid combination
                res.append(list(stack))
                return
            
            for i in range(start_index, len(candidates)):
                # If the candidate is larger than the remaining target,
                # since the array is sorted, all subsequent candidates will also be larger.
                if candidates[i] > remain:
                    break
                
                # Choose the candidate
                stack.append(candidates[i])
                # Backtrack with the same start_index because we can reuse elements
                backtrack(remain - candidates[i], stack, i)
                # Remove the candidate (un-choose)
                stack.pop()
                
        backtrack(target, [], 0)
        return res
