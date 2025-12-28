from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0
        
        while left < right:
            # We process the side with the smaller boundary height
            if height[left] < height[right]:
                # Update left_max or calculate trapped water
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
            else:
                # Update right_max or calculate trapped water
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
                
        return res
