class Solution:
    def firstUniqChar(self, s: str) -> int:
        found = {}
        for i in range(len(s)):
            if s[i] not in found:
                found[s[i]] = 1
            else:
                found[s[i]] += 1
        for f in found:
            if found[f] == 1:
                return s.index(f)
        return -1


