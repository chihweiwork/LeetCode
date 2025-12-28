from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort candidates to handle duplicates and for pruning
        candidates.sort()
        res = []
        
        def backtrack(remain, stack, start_index):
            if remain == 0:
                res.append(list(stack))
                return
            
            for i in range(start_index, len(candidates)):
                # Pruning: if current candidate is already larger than remain, stop
                if candidates[i] > remain:
                    break
                
                # Skip duplicate elements at the same level of the recursion tree
                # This ensures we don't pick the same number twice for the same position
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                stack.append(candidates[i])
                # Recurse with i + 1 as we can only use each element once
                backtrack(remain - candidates[i], stack, i + 1)
                stack.pop()
                
        backtrack(target, [], 0)
        return res
