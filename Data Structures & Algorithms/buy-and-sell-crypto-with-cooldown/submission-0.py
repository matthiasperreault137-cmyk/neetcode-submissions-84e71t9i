class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}


        def dfs(i, state):
            if i >= len(prices):
                return 0
            if (i, state) in dp:
                return dp[(i,state)]

            if state == 1:
                dp[(i,state)] = max((dfs(i + 1, -1) + prices[i]), dfs(i + 1, 1))
                return dp[(i,state)]
            if state == 0:
                dp[(i,state)] = max((dfs(i + 1, 1) - prices[i]), dfs(i +1, 0))
                return dp[(i,state)]
            if state == -1:
                dp[(i,state)] = dfs(i + 1, 0)
                return dp[(i,state)]
            return -9999999999
        return dfs(0,0)