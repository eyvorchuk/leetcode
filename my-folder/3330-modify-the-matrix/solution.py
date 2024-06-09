class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        for j in range(cols):
            neg = []
            max_val = -1
            for i in range(rows):
                if matrix[i][j] > max_val:
                    max_val = matrix[i][j]
                elif matrix[i][j] == -1:
                    neg.append(i)
            for n in neg:
                matrix[n][j] = max_val
        return matrix
