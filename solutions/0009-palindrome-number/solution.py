class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x >= 0 and x < 10:
            return True
        n_digits = int(math.log10(x))+1
        for n in range(1, n_digits // 2 + 1):
            if (x // (10**(n-1))) % 10 != (x // (10**(n_digits - n))) % 10:
                return False
        return True
