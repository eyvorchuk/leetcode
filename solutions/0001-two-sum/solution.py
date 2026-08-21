class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for (i,n) in enumerate(nums):
            if target - n in vals:
                return [i, vals[target - n]]
            if n not in vals:
                vals[n] = i
        
