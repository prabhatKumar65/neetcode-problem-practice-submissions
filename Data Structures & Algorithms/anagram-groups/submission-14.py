class Solution:
    def groupAnagrams(self, strs):

        groups = {}

        for word in strs:

            # Sort the word and make it a string
            key = "".join(sorted(word))

           
            if key not in groups:
                groups[key] = []

            # Add word to its group
            groups[key].append(word)

       
        return list(groups.values())