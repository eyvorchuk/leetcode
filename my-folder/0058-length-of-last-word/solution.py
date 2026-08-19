class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if " " not in s:
            return len(s)
        length = 0
        space_start = True
        for n in range(1, len(s)+1):
            char = s[-1*n]
            if not space_start and char == " ":
                return length
            if char != " ":
                space_start = False
                length += 1
        return length
