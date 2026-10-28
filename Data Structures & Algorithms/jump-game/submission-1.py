class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: 
            return false
        seen = {}
        def jump(i):
            if i >= len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            for num in range(nums[i] + i, i, -1):
                if num in seen and seen[num] == False:
                    continue 
                if jump(num):
                    return True
                else:
                    seen[num] = False
            return False
        return jump(0)
