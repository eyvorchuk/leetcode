class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alpha = ""
        for c in s:
            asc = ord(c.lower())
            if (asc >= 48 and asc <= 57) or (asc >= 97 and asc <= 122):
                s_alpha += c.lower()
        for i in range(len(s_alpha) // 2):
            if s_alpha[i] != s_alpha[-1*(i+1)]:
                return False
        return True
