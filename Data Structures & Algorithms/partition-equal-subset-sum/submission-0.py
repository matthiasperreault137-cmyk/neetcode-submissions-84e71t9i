class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        vals = set()
        vals.add(0)
        total = 0
        for j in range(len(nums)):
            total += nums[j]
        target = total / 2
        for i in range(len(nums)):
            num = nums[i]
            newVals = []
            for val in vals:
                newVal = val + num
                if newVal == target:
                    return True
                if newVal not in vals:
                    newVals.append(newVal)
            for k in range(len(newVals)):
                newVal = newVals[k]
                vals.add(newVal)
        return False