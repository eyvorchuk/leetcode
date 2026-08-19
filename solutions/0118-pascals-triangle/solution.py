class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for n in range(numRows):
            if n == 0:
                triangle.append([1])
            elif n == 1:
                triangle.append([1,1])
            else:
                row = [1]
                last = triangle[-1]
                for i in range(1, len(last)):
                    row.append(last[i] + last[i-1])
                row.append(1)
                triangle.append(row)
        return triangle

