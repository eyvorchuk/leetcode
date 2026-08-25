class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_dict = {}
        for n in nums:
            num_dict[n] = 1
        mult = k
        while True:
            if mult not in num_dict:
                return mult
            mult += k
