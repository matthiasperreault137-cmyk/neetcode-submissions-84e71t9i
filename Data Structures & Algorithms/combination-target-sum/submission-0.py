class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        solution = []
        def DFS(i, sum, path):
            if sum == target:
                solution.append(path.copy())
                return
            if sum > target:
                return 
            

            for j in range(i, len(nums)):
                num = nums[j]
                sum += num
                path.append(num)
                DFS(j, sum, path)
                sum -= num
                path.pop()
                
        DFS(0, 0, [])
        return solution