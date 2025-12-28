from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Number of jumps performed
        jumps = 0
        # The farthest position reachable with the current number of jumps
        current_jump_end = 0
        # The farthest position reachable with one more jump
        farthest = 0
        
        # We don't need to process the last element because once we reach
        # current_jump_end >= last_index, we are done.
        for i in range(len(nums) - 1):
            # Update the farthest position we can reach
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of the current jump range
            if i == current_jump_end:
                # We MUST jump
                jumps += 1
                # The next range ends at the farthest position we found
                current_jump_end = farthest
                
                # If we can already reach the end, we can stop early
                if current_jump_end >= len(nums) - 1:
                    break
                    
        return jumps
