class Solution:
    def twoSum( self, nums, target):
        seen =  {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                return [seen[difference], i]
            seen[num] = i    

