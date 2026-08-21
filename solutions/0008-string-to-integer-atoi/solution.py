class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        digits = ""
        
        while i < len(s):
            if s[i] == " ":
                i += 1
            else:
                break
        if i == len(s):
            return 0
        
        negative = s[i] == "-"
        if s[i] in ["-", "+"]:
            i += 1
        
        while i < len(s):
            if s[i] == "0":
                i += 1
            else:
                break
        
        while i < len(s):
            try:
                digit = int(s[i])
                digits += s[i]
                i += 1
            except:
                break
        if digits == "":
            return 0
        
        intS = 0
        for (i,d) in enumerate(digits[::-1]):
            intS += 10**i * int(d)
        if negative:
            intS *= -1
        if intS < -2**31:
            intS = -2**31
        elif intS > 2**31 - 1:
            intS = 2**31 -1
        return intS
            

