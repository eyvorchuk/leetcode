class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target <= nums[0]:
                return 0
            else:
                return 1
        half = len(nums) // 2
        pivot = nums[half]
        if pivot == target:
            return half
        else:
            if target < pivot:
                return self.searchInsert(nums[:half], target) 
            else:
                return half + self.searchInsert(nums[half:], target)


