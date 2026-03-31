class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastNum = None
        newNums = []
        for num in nums:
            if lastNum != num :
                newNums.append(num)
            lastNum = num
        for i in range(len(newNums)):
            nums[i] = newNums[i]
        del nums[len(newNums):]
        return len(newNums)
