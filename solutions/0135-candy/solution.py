class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        candies = [1] * len(ratings)
        for i in range(1, len(ratings) - 1):
            if ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                candies[i] = candies[i - 1] + 1
        if ratings[-1] > ratings[-2] and candies[-1] <= candies[-2]:
            candies[-1] = candies[-2] + 1
        for i in reversed(range(1, len(ratings) - 1)):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        if ratings[0] > ratings[1] and candies[0] <= candies[1]:
                candies[0] = candies[1] + 1
        return sum(candies)
