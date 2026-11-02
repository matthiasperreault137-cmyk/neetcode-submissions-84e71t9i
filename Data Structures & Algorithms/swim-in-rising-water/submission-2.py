class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        nbs = [(1,0), (0,1), (-1,0), (0,-1)]
        highest = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                highest = max(grid[i][j], highest)

        heights = []
        for i in range(highest + 1):
            heights.append([])
        heights[max(grid[len(grid) - 1][len(grid) - 1], grid[0][0])].append((0,0))
        added = set()
        def dfs(stack, height):
            parents = {(0,0) : None}
            while stack:
                node = stack.pop()
                if node == (len(grid) - 1, len(grid) - 1):
                    return True
                for nb in nbs:
                    x = nb[0] + node[0]
                    y = nb[1] + node[1]
                    newNode = (x, y)
                    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid):
                        continue
                    if grid[x][y] > height:
                        if newNode not in added:
                            heights[grid[x][y]].append(newNode)
                            added.add(newNode)
                    else:
                        if newNode in parents:
                            continue
                        parents[newNode] = node
                        stack.append(newNode)
            return False
        for i in range(max(grid[len(grid) - 1][len(grid) - 1], grid[0][0]), len(heights)):
            if dfs(heights[i], i):
                return i
        print("fuckyou didnt work")
        return -1