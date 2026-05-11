class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        results.append([])
        def subs(numbers, num):
            n = len(numbers)
            for i in range(n):
                temp = numbers[i].copy()
                temp.append(num)
                numbers.append(temp)
            return numbers
        for i in range(len(nums)):
            temp = subs(results, nums[i])
            results = temp
        return results
                 
            