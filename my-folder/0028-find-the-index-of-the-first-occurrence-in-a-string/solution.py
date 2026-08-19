class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        split = haystack.split(needle)
        return len(split[0])
