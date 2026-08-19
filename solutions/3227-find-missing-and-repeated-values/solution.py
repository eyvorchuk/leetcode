class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        tot = len(grid)**2
        exp_sum = (tot*(tot+1))//2
        real_sum = 0
        uniques = {}
        dupe = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                n = grid[i][j]
                real_sum += n
                if dupe == -1:
                    if n not in uniques.keys():
                        uniques[n] = 0
                    else:
                        dupe = n
        missing = exp_sum - real_sum + dupe
        return [dupe, missing]
