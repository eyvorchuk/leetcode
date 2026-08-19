class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1 = s[:len(s) // 2]
        s2 = s[len(s) // 2:]
        vowels = ["a", "e", "i", "o", "u"]
        v1 = 0
        v2 = 0
        for i in range(len(s1)):
            if s1[i].lower() in vowels:
                v1 += 1
            if s2[i].lower() in vowels:
                v2 += 1
        return v1 == v2
