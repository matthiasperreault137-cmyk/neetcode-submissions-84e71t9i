class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minMap = {}
        def minCost(step):
            if step >= len(cost):
                return 0
            if step == len(cost) - 1 or step == len(cost) - 2:

                return cost[step]
            val1, val2 = None, None
            if step + 1 in minMap:
                val1 = minMap[step + 1]
            else:
                val1 = minCost(step + 1)
            if step + 2 in minMap:
                val2 = minMap[step + 2]
            else:
                val2 = minCost(step + 2)
            minVal =  cost[step] + min(val1, val2)
            minMap[step] = minVal
            return minVal
        return min(minCost(0), minCost(1))