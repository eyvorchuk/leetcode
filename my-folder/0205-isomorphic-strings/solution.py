class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chars_s = {}
        chars_t = {}
        for i in range(len(s)):
            if s[i] not in chars_s:
                chars_s[s[i]] = t[i]
            elif chars_s[s[i]] != t[i]:
                return False
            if t[i] not in chars_t:
                chars_t[t[i]] = s[i]
            elif chars_t[t[i]] != s[i]:
                return False
        return True
