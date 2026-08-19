class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        while True:
            n = sum([int(d)**2 for d in str(n)])
            if n in seen:
                return False
            elif n == 1:
                return True
            seen[n] = 0

