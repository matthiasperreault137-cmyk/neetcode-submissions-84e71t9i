class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        def DFS(i, path, seen):
            if len(path) == len(nums):
                solution.append(path.copy())
                return
            for j in range(0, len(nums)):
                if j in seen:
                    continue
                num = nums[j]
                path.append(num)
                seen.add(j)
                DFS(j, path, seen)
                path.pop()
                seen.remove(j)                
        DFS(0, [], set())
        return solution