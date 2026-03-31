class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = 1
        left = 1
        zeronum = 0
        results = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeronum += 1
        if zeronum == 0:
            for i in range(1, len(nums)):
                right *= nums[i]
            for i in range(len(nums)):
                results.append(left * right)
                left *= nums[i]
                if i + 1 < len(nums):
                    right //= nums[i + 1]
                else:
                    right = 1
            return results
        elif zeronum > 1:
            for i in range(len(nums)):
                results.append(0)
            return results
        else:
            factor = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    factor *= nums[i]
            for i in range(len(nums)):
                if nums[i] != 0:
                    results.append(0)
                else:
                    results.append(factor)
            return results