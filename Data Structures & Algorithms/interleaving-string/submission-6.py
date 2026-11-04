class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        for i in range(len(s1) + 2):
            for j in range(len(s2) + 2):
                dp[(i, j)] = 0
        
        if len(s1) +len(s2) != len(s3):
            return False
        dp[(len(s1), len(s2))] = 1
        for i in range(len(s1), -1 ,-1):
            for j in range(len(s2), -1, -1):
                if i == len(s1) and j == len(s2):
                    continue
                c = len(s1) - i + len(s2) - j
                char = s3[-c]
                if i < len(s1) and char == s1[i] and dp[(i + 1,j)] == 1:
                    dp[(i, j)] = 1
                elif j < len(s2) and char == s2[j] and dp[(i , j + 1)] == 1:
                    dp[(i, j)] = 1
                else:
                    dp[(i, j)] = 0
        return dp[(0,0)] == 1