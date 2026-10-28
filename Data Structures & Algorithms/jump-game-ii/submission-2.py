class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        total = 0
        while i < len(nums) - 1:
            if i + nums[i] >= len(nums) - 1:
                return total + 1
            total += 1
            num = nums[i]

            far = 0
            best = 0
            for j in range(i + 1, min(len(nums), num + i + 1)):
                if far >= nums[j] + j:

                    continue
                else:
                    best = j
                    far = nums[j] + j
            i = best
        return total