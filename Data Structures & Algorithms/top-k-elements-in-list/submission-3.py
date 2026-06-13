class Solution:
    def topKFrequent(self, nums, k):

        # Store frequency of each number
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Sort by frequency (highest first)
        sorted_items = sorted(
            count.items(),
            key=lambda item: item[1],
            reverse=True
        )

        result = []

        # Take first k elements
        for i in range(k):
            result.append(sorted_items[i][0])

        return result