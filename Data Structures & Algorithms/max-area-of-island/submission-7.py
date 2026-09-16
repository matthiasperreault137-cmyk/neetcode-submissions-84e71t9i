class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        maxIsland = 0
        def BFSCount(position):
            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            toVisit = deque()
            toVisit.append(position)
            explored = set()
            explored.add(position)
            total = 0
            print("starting BFS from" + "x" + str(position[0]) + "y" + str(position[1]))
            while toVisit:
                pos = toVisit.popleft()
                total += 1
                seen.add(pos)
                for neighbor in neighbors:
                    x = neighbor[0] + pos[0]
                    y = neighbor[1] + pos[1]
                    if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[x]) - 1:
                        continue
                    node = grid[x][y]
                    if not node or (x,y) in explored:
                        continue
                    else:
                        explored.add((x,y))
                        toVisit.append((x,y))
            return total
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                node = grid[i][j]
                if not node or (i,j) in seen:
                    continue
                    print("skipped")
                else:
                    maxIsland = max(BFSCount((i, j)), maxIsland)
        return maxIsland