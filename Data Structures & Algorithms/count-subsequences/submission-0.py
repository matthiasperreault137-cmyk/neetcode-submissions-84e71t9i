class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        for i in range(len(s) + 1):
            for j in range(len(t) + 1):
                if j == len(t):
                    dp[(i,j)] = 1
                else:
                    dp[(i,j)] = 0
        for a in range(len(s) -1, -1, -1):
            for b in range(len(t) - 1, -1 ,-1):
                char1 = s[a]
                char2 = t[b]

                if char1 == char2:
                    dp[(a,b)] = dp[(a + 1, b + 1)] + dp[(a + 1, b)]
                else:
                    dp[(a, b)] = dp[(a + 1, b)]
        return dp[(0,0)]