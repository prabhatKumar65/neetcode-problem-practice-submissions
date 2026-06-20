class Solution:
    def isPalindrome(self, s):

        # Left pointer will run from start
        left = 0

        # Right pointer will run from end
        right = len(s) - 1

        while left < right:

            # Skip non-alphanumeric character from left side
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric character from right side
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters after converting to lowercase
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers
            left += 1
            right -= 1

        return True