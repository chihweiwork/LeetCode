from typing import List

class Solution:
  def maxArea(self, height: List[int]) -> int:
    """
    Finds the two lines that together with the x-axis form a container,
    such that the container contains the most water.

    This problem is solved efficiently using the two-pointer technique.
    """
    max_area = 0
    left, right = 0, len(height) - 1

    while left < right:
      # The area is determined by the shorter line (the bottleneck) and the distance.
      h = min(height[left], height[right])
      w = right - left
      current_area = h * w
      max_area = max(max_area, current_area)

      # To find a potentially larger area, we need to move the pointer
      # of the shorter line. Moving the taller line's pointer inward will
      # always result in a smaller or equal area because the width (w)
      # decreases and the height (h) is still limited by the shorter line.
      if height[left] < height[right]:
        left += 1
      else:
        right -= 1
        
    return max_area
