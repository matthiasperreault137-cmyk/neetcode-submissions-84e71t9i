class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        nbs = []
        for _ in range(n):
            nbs.append([])
        for edge in flights:
            node1 = edge[0]
            node2 = edge[1]
            cost = edge[2]
            nbs[node1].append([node2, cost])
        dp = {}
        def dfs(node, remaining):
            if node == dst:
                return 0
            if remaining == -1:
                return -1
            lowest = float('inf')
            for nb in nbs[node]:
                cost = nb[1]
                i = nb[0]
                dpVal = (i,remaining - 1)
                if dpVal in dp:
                    if dp[dpVal] == -1:
                        continue
                    lowest = min(lowest, dp[dpVal] + cost)
                else:
                    dfsVal = dfs(i, remaining - 1)
                    if dfsVal == -1:
                        continue
                    else:
                        lowest = min(lowest, dfsVal + cost)
            if lowest < float('inf'):
                dp[(node, remaining)] = lowest
                return lowest
            dp[(node, remaining)] = -1
            return -1
        return dfs(src, k)