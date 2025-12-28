class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # We use a stack to store the indices of the parentheses.
        # We initialize the stack with -1 to serve as a boundary.
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of '(' onto the stack
                stack.append(i)
            else:
                # We found a ')', pop the top element
                stack.pop()
                if not stack:
                    # If the stack is empty, it means this ')' doesn't have a matching '('
                    # We push its index as the new boundary
                    stack.append(i)
                else:
                    # The length of the current valid substring is 
                    # (current index - index of the previous unmatched element)
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len
