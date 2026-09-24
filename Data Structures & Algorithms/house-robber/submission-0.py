class Solution:
    def rob(self, nums: List[int]) -> int:
        valMap = {}

        def MaxVal(house):
            print("yo")
            if house >= len(nums):
                return 0
            if house == len(nums) - 1 or house == len(nums) - 2:
                return nums[house]
            val1 = 0
            for i in range(house + 2, len(nums)):
                if i in valMap:
                    val1 = max(val1, valMap[i])
                else:
                    val1 = max(val1, MaxVal(i))
            total = val1 + nums[house]
            valMap[house] = total
            return total
        best = max(MaxVal(1), MaxVal(0))
        return best