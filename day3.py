class Solution(object):
    def twoSum(self, nums, target):
        
        seen = {}
        
        for i, num in enumerate(nums):
            if target - num in seen:
                return ([seen[target - num], i])
            elif num not in seen:
                seen[num] = i

