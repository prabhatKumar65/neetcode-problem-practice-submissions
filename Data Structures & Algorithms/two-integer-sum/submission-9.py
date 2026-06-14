class Solution:
    def twoSum(self, nums, target):

       
        seen = {}

        
        for i, num in enumerate(nums):

            # Find required number
            difference = target - num

            # Check if required number already exists
            if difference in seen:

                # Return previous index and current index
                return [seen[difference], i]

            # Store current number and its index
            seen[num] = i