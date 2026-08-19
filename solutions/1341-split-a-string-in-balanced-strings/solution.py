class Solution:
    def balancedStringSplit(self, s: str) -> int:
        maxSubstrings = 0
        start = 0
        push = ""
        for c in s:
            if start == 0:
                push = c
                start += 1
            else:
                if c != push:
                    start -= 1
                    if start == 0:
                        maxSubstrings += 1
                else:
                    start += 1
        return maxSubstrings
            
