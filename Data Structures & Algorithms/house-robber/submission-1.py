class Solution:
    def rob(self, nums: List[int]) -> int:
        valMap = {}

        def MaxVal(house):
            print("yo")
            if house >= len(nums):
                return 0
            if house == len(nums) - 1 or house == len(nums) - 2:
                return nums[house]
            val1, val2 = 0, 0
            if house + 2 in valMap:
                val1 = valMap[house + 2]
            else:
                val1 = MaxVal(house + 2)
            if house + 3 in valMap:
                val2 = valMap[house + 3]
            else:
                val2 = MaxVal(house + 3)
            total = max(val1, val2) + nums[house]
            valMap[house] = total
            return total
        best = max(MaxVal(1), MaxVal(0))
        return best