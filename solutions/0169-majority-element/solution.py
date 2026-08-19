class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n,0)
            if counts[n] > length // 2:
                return n
