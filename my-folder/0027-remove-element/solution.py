class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0
        for n in nums:
            if n != val:
                nums[pos] = n
                pos += 1
        return pos
