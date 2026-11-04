class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i,q):
            if q == amount:
                return 1
            if q > amount:
                return 0
            if i >= len(coins):
                return 0

            if (i, q) in dp:
                return dp[(i, q)]
            total = dfs(i, q + coins[i]) + dfs(i + 1, q)
            dp[(i,q)] = total
            return total
        return dfs(0,0)