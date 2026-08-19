class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        pos = 0
        while pos < len(s):
            if s[pos] == "I":
                if pos+1 < len(s) and s[pos+1] == "V":
                    num += 4
                    pos += 2
                elif pos+1 < len(s) and s[pos+1] == "X":
                    num += 9
                    pos += 2
                else:
                    num += 1
                    pos += 1
            elif s[pos] == "X":
                if pos+1 < len(s) and s[pos+1] == "L":
                    num += 40
                    pos += 2
                elif pos+1 < len(s) and s[pos+1] == "C":
                    num += 90
                    pos += 2
                else:
                    num += 10
                    pos += 1
            elif s[pos] == "C":
                if pos+1 < len(s) and s[pos+1] == "D":
                    num += 400
                    pos += 2
                elif pos+1 < len(s) and s[pos+1] == "M":
                    num += 900
                    pos += 2
                else:
                    num += 100
                    pos += 1
            else:
                inc = {"V": 5, "L": 50, "D": 500, "M": 1000}
                num += inc[s[pos]]
                pos += 1
        return num
