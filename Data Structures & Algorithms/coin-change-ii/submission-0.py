class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i,q):
            if q == amount:
                return 1
            if i >= len(coins):
                return 0

            if (i, q) in dp:
                return dp[(i, q)]
            
            total = 0
            for j in range(((amount - q)//coins[i]) + 1):
                total += dfs(i + 1, q + (coins[i] * j))
            dp[(i, q)] = total
            return total
        return dfs(0,0)