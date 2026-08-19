import numpy

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = list(collections.Counter(arr).values())
        return len(counts) == numpy.unique(counts).size
