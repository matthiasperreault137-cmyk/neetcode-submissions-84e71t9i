class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1
        while l <= r and t <= b:
            if l == r and  b == t:
                res.append(matrix[t][l])
                break
            elif b == t:
                for i in range(r - l + 1):
                    res.append(matrix[t][l + i])
            elif l == r:
                for j in range(b - t + 1):
                    res.append(matrix[t + j][r])
            else:
                for i in range(r - l):
                    res.append(matrix[t][l + i])
                for j in range(b - t):
                    res.append(matrix[t + j][r])
                for k in range(r - l):
                    res.append(matrix[b][r - k])
                for h in range(b - t):
                    res.append(matrix[b - h][l])
            l += 1
            t += 1
            r -= 1
            b -= 1
        return res