class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = False 
        c = False 
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i == 0:
                        c = True
                    if j == 0:
                        r = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0


        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if c:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if r:
            for i in range(len(matrix)):
                matrix[i][0] = 0