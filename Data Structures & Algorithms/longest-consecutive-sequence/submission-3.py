class Solution:
    def longestConsecutive(self, nums):

        # Convert list to set for fast lookup
        num_set = set(nums)

        # Store longest sequence length
        longest = 0

        # Check every number
        for num in num_set:

            # Start only if previous number does not exist
            if num - 1 not in num_set:

                current_num = num
                current_length = 1

                # Keep checking next consecutive numbers
                while current_num + 1 in num_set:

                    current_num += 1
                    current_length += 1

                # Update longest length
                longest = max(longest, current_length)

        return longest