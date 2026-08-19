class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            last = self.getRow(rowIndex-1)
            row = [1]
            for i in range(1, len(last)):
                row.append(last[i]+last[i-1])
            row.append(1)
            return row
