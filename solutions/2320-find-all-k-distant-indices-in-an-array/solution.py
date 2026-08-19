class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        k_distant = {}
        for i in range(len(nums)):
            if nums[i] == key:
                min_index = max(i-k, 0)
                max_index = min(i+k, len(nums) - 1)
                for j in range(min_index, max_index+1):
                    k_distant[j] = 0
        return k_distant.keys()
