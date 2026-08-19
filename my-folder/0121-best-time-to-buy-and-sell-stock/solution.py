class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                prof = max(prof, sell-buy)
            else:
                buy = sell
        return prof
