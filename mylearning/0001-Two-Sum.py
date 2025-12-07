def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    length = len(nums)
    for i1 in range(length):
        s1 = nums[i1]
        i2 = i1 + 1
        while i2 < length:
            s2 = nums[i2]
            if target == s1 + s2:
                print([i1, i2])
                return [i1, i2]
            i2 += 1



twoSum(nums = [2,7,11,15], target = 9)
twoSum(nums = [3,2,4], target = 6)
twoSum(nums = [3,3], target = 6)
