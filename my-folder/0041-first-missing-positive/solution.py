class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n_nums = len(nums)
        for i in range(n_nums):
            if nums[i] <= 0:
                nums[i] = n_nums + 1
        for i in range(n_nums):
            if abs(nums[i]) - 1 < n_nums and nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -1 * nums[abs(nums[i]) - 1]
        print(nums)
        for i in range(1, n_nums + 1):
            if nums[i - 1] > 0:
                return i
        return n_nums + 1

        
