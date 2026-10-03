class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest = 0
        dp = {}
        for i in range(len(nums) - 1, -1, - 1):
            total = 0
            last = -10001
            for j in range(i, len(nums)):
                num = nums[j]
                if j in dp:
                    #maybe extra check is required and also inverse seen and dp checks
                    if num > last:
                        total += dp[j]
                        longest = max(longest, total)
                        if i in dp:
                            dp[i] = max(dp[i], total)
                        else:
                            dp[i] = total
                        total -= dp[j]
                        continue
                if num > last:
                    total += 1
                    last = num
                if j == len(nums) - 1:
                    if i in dp:
                        dp[i] = max(dp[i], total)
                    else:
                        dp[i] = total
                    break
        if longest == 0:
            return 1
        return longest

