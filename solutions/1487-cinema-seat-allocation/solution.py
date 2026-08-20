class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedRows = {}
        numReservedRows = 0
        for seat in reservedSeats:
            if seat[0] not in reservedRows:
                numReservedRows += 1
                reservedRows[seat[0]] = [seat[1]]
            else:
                reservedRows[seat[0]].append(seat[1])
        unreservedRows = n - numReservedRows
        maxNum = 2 * unreservedRows
        for row in reservedRows:
            seatsInRow = reservedRows[row]
            if 2 not in seatsInRow:
                groupReserved = False
                for i in range(3, 6):
                    if i in seatsInRow:
                        groupReserved = True
                        break
                if not groupReserved:
                    maxNum += 1
                    if 6 not in seatsInRow:
                        for i in range(6, 10):
                            if i in seatsInRow:
                                groupReserved = True
                                break
                        if not groupReserved:
                            maxNum += 1
                            continue
                    continue
            
            if 4 not in seatsInRow:
                groupReserved = False
                for i in range(5, 8):
                    if i in seatsInRow:
                        groupReserved = True
                        break
                if not groupReserved:
                    maxNum += 1
                    continue
            
            if 6 not in seatsInRow:
                groupReserved = False
                for i in range(6, 10):
                    if i in seatsInRow:
                        groupReserved = True
                        break
                if not groupReserved:
                    maxNum += 1 
        return maxNum
                    
