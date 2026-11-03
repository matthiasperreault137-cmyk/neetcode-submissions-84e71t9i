class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = len(nums) - 1, 0
        while j < i:
            while nums[j] != val and j < i :
                j += 1
            while nums[i] == val and j < i:
                i -= 1
            if j >= i:
                break
            nums[i], nums[j] = nums[j], nums[i]
        total = 0
        for k in range(len(nums)):
            if nums[k] != val:
                total += 1
        return total