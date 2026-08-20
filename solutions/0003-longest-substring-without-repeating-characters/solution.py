class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        MAX_LENGTH = 100
        max_length = 1
        for (i, c) in enumerate(s):
            foundChars = {c: 1}
            curr_length = 1
            for c2 in s[i+1:]:
                if c2 in foundChars:
                    break
                foundChars[c2] = 1
                curr_length += 1
            if curr_length > max_length:
                max_length = curr_length
                if max_length == MAX_LENGTH:
                    return MAX_LENGTH
        return max_length

