from typing import List

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    """
    Finds all unique triplets in the array which gives the sum of zero.
    
    The key to an efficient solution (O(n^2)) is to first sort the array,
    and then use a two-pointer approach.
    """
    result = []
    # 1. Sort the array. This is crucial for the two-pointer approach
    #    and for skipping duplicates.
    nums.sort()
    
    n = len(nums)
    
    # 2. Iterate through the array with the first pointer 'i'.
    for i in range(n - 2):
      # 3. Skip positive integers for the first element.
      #    If the smallest number is > 0, the sum of three cannot be 0.
      if nums[i] > 0:
        break
        
      # 4. Skip duplicate first elements to avoid duplicate triplets.
      #    If the current element is the same as the one before, we have
      #    already processed this case.
      if i > 0 and nums[i] == nums[i-1]:
        continue
      
      # 5. Initialize two pointers, 'left' and 'right'.
      left, right = i + 1, n - 1
      
      # 6. Use the two-pointer technique to find the other two numbers.
      while left < right:
        total = nums[i] + nums[left] + nums[right]
        
        if total < 0:
          # Sum is too small, need a larger number.
          left += 1
        elif total > 0:
          # Sum is too large, need a smaller number.
          right -= 1
        else:
          # Found a triplet!
          result.append([nums[i], nums[left], nums[right]])
          
          # 7. Skip duplicates for the second and third elements.
          #    Move 'left' pointer forward while it's pointing to a duplicate.
          while left < right and nums[left] == nums[left + 1]:
            left += 1
          # Move 'right' pointer backward while it's pointing to a duplicate.
          while left < right and nums[right] == nums[right - 1]:
            right -= 1
            
          # Move pointers to find the next potential triplet.
          left += 1
          right -= 1
          
    return result
