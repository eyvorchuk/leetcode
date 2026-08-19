class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counts = collections.Counter(nums)
        pairs = 0
        left = 0
        for c in counts.values():
            pairs += c // 2
            left += c % 2
        return [pairs, left]
