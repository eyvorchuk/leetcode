class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = collections.Counter(nums)
        i = 0
        keys = [0,1,2]
        for k in keys:
            for j in range(counts[k]):
                nums[i] = k
                i += 1
        
        
