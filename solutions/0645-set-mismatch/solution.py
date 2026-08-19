class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_nums = sum(nums)
        exp_sum = (n*(n+1))//2
        sum_square = sum([i**2 for i in nums])
        exp_sum_square = (n*(n+1)*(2*n+1))//6
        lr_diff = exp_sum - sum_nums
        diff_squares = exp_sum_square - sum_square
        lr_sum = diff_squares // lr_diff
        loss = (lr_diff + lr_sum) // 2
        rep = lr_sum - loss
        return [rep, loss]
