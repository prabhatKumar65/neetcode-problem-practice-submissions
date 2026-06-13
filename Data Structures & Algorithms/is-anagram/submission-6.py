class Solution:
    def isAnagram(self, s, t):

        # Check if both strings have same length
        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Dictionary to store character counts
        count = {}

        # Count frequency of each character in string s
        for char in s:

            # If character already exists, increase count
            if char in count:
                count[char] = count[char] + 1

            # If character appears first time, set count to 1
            else:
                count[char] = 1

        # Check characters of string t
        for char in t:

            # Character not found in dictionary
            # Means strings are not anagrams
            if char not in count:
                return False

            # Decrease count for matched character
            count[char] = count[char] - 1

            # Negative count means extra character in t
            if count[char] < 0:
                return False

        # All checks passed
        # Strings are anagrams
        return True