from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        res = []
        
        def backtrack(index: int, current_path: str):
            # If the combination is complete
            if len(current_path) == len(digits):
                res.append(current_path)
                return
            
            # Get the letters that the current digit maps to
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                # Add the letter and move on to the next digit
                backtrack(index + 1, current_path + letter)
                
        backtrack(0, "")
        return res
