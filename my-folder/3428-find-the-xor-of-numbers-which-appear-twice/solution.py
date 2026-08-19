class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        dupes = []
        uniques = {}
        for n in nums:
            if n not in uniques.keys():
                uniques[n] = 0
            else:
                dupes.append(n)
        if len(dupes) == 1:
            return dupes[0]
        elif len(dupes) == 0:
            return 0
        xor = dupes[0]
        for n in dupes[1:]:
            xor = xor^n
        return xor
            
