class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        far = 0
        for i in range(len(nums)):
            num = nums[i]
            if i >= far and num == 0 and i != len(nums) -1:
                return False
            else:
                far = max(far, i + num)
        return True