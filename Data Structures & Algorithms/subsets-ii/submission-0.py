class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        results.append([])
        count = 0

        def subsets(lastAdded, numbers, num, prev):
            n = len(numbers)
            counter = 0
            if prev and prev == num:
                i = n - lastAdded
                for j in range(i, n):
                    temp = numbers[j].copy()
                    temp.append(num)
                    numbers.append(temp)
                    counter += 1
            else:
                for j in range(n):
                    temp = numbers[j].copy()
                    temp.append(num)
                    numbers.append(temp)
                    counter += 1
            added = (numbers, counter)
            return added
        for i in range(len(nums)):
            tempNums, tempCount = None,None
            if i - 1 == -1:
                tempNums, tempCount = subsets(count, results, nums[i], None)
            else:
                tempNums, tempCount = subsets(count, results, nums[i], nums[i - 1])
            results = tempNums
            count = tempCount

        return results