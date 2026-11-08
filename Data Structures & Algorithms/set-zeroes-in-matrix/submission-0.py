class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        columns = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows or j in columns:
                    matrix[i][j] = 0
        return
