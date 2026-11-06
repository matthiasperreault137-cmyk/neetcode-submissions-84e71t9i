class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}

        nums.insert(0, 1)
        nums.append(1)
        for i in range(len(nums)-1):
            j = i + 1
            dp[(i,j)] = 0

        for b in range(2, len(nums)):
            for a in range(len(nums) - b):
                i = a
                j = a + b
                biggieCheese = 0
                for k in range(i + 1, j):
                    left = dp[(i, k)]
                    right = dp[(k ,j )]
                    val = nums[i] * nums[j] * nums[k]
                    biggieCheese = max(biggieCheese, left + right + val)
                dp[(i,j)] = biggieCheese
        return dp[(0, len(nums) - 1)]
            
