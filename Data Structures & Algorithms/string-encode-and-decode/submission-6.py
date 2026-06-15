class Solution:

    def encode(self, strs):

        encoded = ""

        for s in strs:

            # Add length + # + actual string
            encoded += str(len(s)) + "#" + s

        return encoded


    def decode(self, s):

        result = []

        i = 0

        while i < len(s):

            # Find #
            j = i

            while s[j] != "#":
                j += 1

           

            length = int(s[i:j])

            # Extract string
            word = s[j + 1 : j + 1 + length]

            result.append(word)

           
            i = j + 1 + length

        return result