class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = {}
        for char in s:
            if char in count:
                count[char] = count[char] + 1
            else:
                count[char] = 1
        for char in t:
            if char not in count:
                return False
            count[char] = count[char] - 1
            if count[char] < 0:
                return False
        return True                        