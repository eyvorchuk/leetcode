class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        if negative:
            x *= -1
        reversed_x = int(str(x)[::-1])
        if negative:
            reversed_x *= -1
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            reversed_x = 0
        return reversed_x 

