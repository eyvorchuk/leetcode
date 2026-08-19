class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        non_div_sum = 0
        div_sum = 0
        for i in range(n+1):
            if i % m == 0:
                div_sum += i
            else:
                non_div_sum += i
        return non_div_sum - div_sum
