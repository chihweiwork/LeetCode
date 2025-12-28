from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(current_s: str, open_count: int, close_count: int):
            # Base case: if the string length reaches 2*n
            if len(current_s) == 2 * n:
                res.append(current_s)
                return
            
            # We can add an opening bracket if we haven't used all n of them
            if open_count < n:
                backtrack(current_s + '(', open_count + 1, close_count)
            
            # We can add a closing bracket if it doesn't exceed the number of opening ones
            if close_count < open_count:
                backtrack(current_s + ')', open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return res
