class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None:
            return None
        maxNum = nums[0]
        current = None
        for num in nums:
            if not current:
                current = num
                continue
            if current < num and current < 0:
                current = num
                maxNum = max(maxNum, current)
            else:
                current += num
                maxNum = max(maxNum, current)
        return maxNum
                