class Solution:
    def isValid(self, s: str) -> bool:
        # If the string has an odd number of characters, it can't be valid
        if len(s) % 2 != 0:
            return False
            
        # Map opening brackets to their corresponding closing brackets
        bracket_map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        stack = []
        
        for char in s:
            if char in bracket_map:
                # It's an opening bracket, push to stack
                stack.append(char)
            else:
                # It's a closing bracket
                # If stack is empty or top doesn't match, it's invalid
                if not stack or bracket_map[stack.pop()] != char:
                    return False
                    
        # If stack is empty, all brackets were correctly matched
        return len(stack) == 0
