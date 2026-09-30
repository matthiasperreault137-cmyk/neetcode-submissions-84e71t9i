class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        cur1 = 1 #max
        cur2 = 1 #min

        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                best = max(best, 0)
                cur1, cur2 = 1, 1
                continue
            temp = cur1
            cur1 = max(num, cur1 * num, cur2 * num)
            cur2 = min(num, temp * num, cur2 * num)
            best = max(best, cur1)
        return best

