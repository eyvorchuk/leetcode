class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        trips = {}
        nums.sort()
        for (i, n) in enumerate(nums[:-2]):
            target = -1 * n
            vals = {}
            for (j, n2) in enumerate(nums[i+1:]):
                if target - n2 in vals:
                    key = (n, n2, target - n2)
                    if key not in trips:
                        trips[key] = 1
                vals[n2] = j
        return [list(k) for k in trips.keys()]
