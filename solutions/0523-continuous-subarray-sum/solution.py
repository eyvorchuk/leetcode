class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        acc_sum = [nums[0]]
        for i in range(1, len(nums)):
            acc_sum.append(nums[i] + acc_sum[i-1])
        mod_sum = [s % k for s in acc_sum]
        try:
            if mod_sum.index(0, 1) > 0:
                return True
        except:
            pass
        unique_mod_sum = {}
        for i in range(len(mod_sum)):
            if mod_sum[i] not in unique_mod_sum.keys():
                unique_mod_sum[mod_sum[i]] = 0
            elif i - mod_sum.index(mod_sum[i]) > 1:
                return True
        return False
            

