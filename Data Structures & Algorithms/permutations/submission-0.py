class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        def DFS(i, path, seen):
            if len(path) == len(nums):
                solution.append(path.copy())
                return
            for j in range(0, len(nums)):
                print(str(j) +" this shit should be in seen so normally im not gopnna see some bulshit about n = adde")
                if j in seen:
                    print("it was seen")
                    continue
                num = nums[j]
                path.append(num)
                seen.add(j)
                print(str(i) + "= i" + "added")
                DFS(j, path, seen)
                path.pop()
                print(str(i) + "= i")
                seen.remove(j)                
        DFS(0, [], set())
        return solution