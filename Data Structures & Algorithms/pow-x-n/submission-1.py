class Solution:
    def myPow(self, x: float, fuckthis: int) -> float:
        dp = {}
        if fuckthis == 0:
            return 1
        def bullshit(n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n in dp:
                return dp[n]
            upperBound = -( n // (-2))
            lowerBound = n // 2
            total = bullshit(lowerBound) * bullshit(upperBound)
            dp[n] = total
            return total
        if fuckthis > 0:
            return bullshit(fuckthis)
        if fuckthis < 0:
            return 1 / bullshit(-fuckthis)
