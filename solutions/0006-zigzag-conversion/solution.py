class Solution:
    def convert(self, s: str, numRows: int) -> str:
        charsInRows = ["" for i in range(numRows)]
        i = 0
        while i < len(s):
            for row in range(numRows):
                charsInRows[row] += s[i]
                i += 1
                if i == len(s):
                    break
            if i < len(s):
                for row in reversed(range(1, numRows - 1)):
                    charsInRows[row] += s[i]
                    i += 1
                    if i == len(s):
                        break
        convertedString = "".join(charsInRows)
        return convertedString
            
        
