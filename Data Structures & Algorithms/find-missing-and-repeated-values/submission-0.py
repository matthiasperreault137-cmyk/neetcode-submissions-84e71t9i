class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        hashset = set()
        result = [0, 0]

        for i in range(n):
            for j in range(n):
                num = grid[i][j]
                if num in hashset:
                    result[0] = num          # repeated
                hashset.add(num)

        for i in range(1, n * n + 1):        # values go from 1 to n²
            if i not in hashset:
                result[1] = i                # missing

        return result