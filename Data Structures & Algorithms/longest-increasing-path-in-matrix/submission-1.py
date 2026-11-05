class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        nbs = [(0,1), (0,-1), (1, 0), (-1, 0)]
        dp = {}
        seen = set()
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            val = matrix[i][j]
            best = 0
            for nb in nbs:
                x = i + nb[0]
                y = j + nb[1]
                if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[x]):
                    continue
                if matrix[x][y] <= val:
                    continue

                best = max(dfs(x,y), best)
            dp[(i ,j)] = best + 1
            return dp[(i,j)]
        result = 0
        for a in range(len(matrix)):
            for b in range(len(matrix[a])):
                result = max(result, dfs(a,b))
        return result