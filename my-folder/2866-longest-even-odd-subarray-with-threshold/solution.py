class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_length = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0 or nums[i] > threshold:
                continue
            length = 1
            for j in range(i+1,len(nums)):
                if nums[j-1] % 2 != nums[j] % 2 and nums[j] <= threshold:
                    length += 1
                else:
                    break
            if length > max_length:
                max_length = length
        return max_length
