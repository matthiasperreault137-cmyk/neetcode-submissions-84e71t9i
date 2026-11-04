class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, q):
            if q == target and i == len(nums):
                return 1
            if i >= len(nums):
                return 0

            if (i, q) in dp:
                return dp[(i, q)]
            total = dfs(i + 1, q - nums[i]) + dfs(i + 1, q + nums[i])
            dp[(i, q)] = total
            return total
        return dfs(0,0)