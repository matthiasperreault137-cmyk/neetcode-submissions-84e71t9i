class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        last = None
        minNum = nums[right]
        while left <= right:
            mid = (left + right) // 2
            minNum = min(nums[mid], minNum)
            if nums[mid] > minNum:
                left = mid + 1
            else:
                right = mid - 1
        return minNum