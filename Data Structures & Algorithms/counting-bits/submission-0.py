class Solution:
    def countBits(self, n: int) -> List[int]:
        offSet = 1
        dp = {}
        dp[0] = 0
        results = [0]
        for i in range(1,n + 1):
            if i / 2 >= offSet:
                offSet  *= 2
            results.append(1 + dp[i - offSet])
            dp[i] = 1 + dp[i - offSet]
        return results