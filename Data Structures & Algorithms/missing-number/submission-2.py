class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp = [i for i in range(len(nums) + 1)]
        res = 0
        for num in nums:
            res ^= num
        for tem in temp:
            res ^= tem
        return res
        