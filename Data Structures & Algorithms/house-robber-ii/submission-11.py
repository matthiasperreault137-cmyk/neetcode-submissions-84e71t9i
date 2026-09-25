class Solution:
    def rob(self, nums: List[int]) -> int:
        def MaxVal(h, l, m):
            if h >= l:
                return 0
            if h == l - 1 or h == l - 2:
                return nums[h]
            val1, val2 = 0 ,0 
            if h + 2 in m:
                val1 = m[h+ 2]
            else:
                val1 = MaxVal(h+ 2,l,m)
            if h + 3 in m:
                val2 = m[h + 3]
            else:
                val2 = MaxVal(h + 3, l, m)
            total = nums[h] + max(val1, val2)
            m[h] = total
            return total
        if len(nums) == 1:
            return nums[0]
        result = max(MaxVal(0, len(nums) - 1, {}), MaxVal(1, len(nums), {}), MaxVal(2, len(nums), {}))
        return result  