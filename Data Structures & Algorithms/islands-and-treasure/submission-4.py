class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
        toVisit = deque()
        

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                val = grid[i][j]
                if val == 0:
                    toVisit.append(((i,j), 0))


        while toVisit:
            popVal = toVisit.popleft()
            pos = popVal[0]
            path = popVal[1]
            for neighbor in neighbors:
                x = pos[0] + neighbor[0]
                y = pos[1] + neighbor[1]
                if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[x]) - 1:
                    continue
                val = grid[x][y]
                if val == 0 or val == -1 or val <= path + 1:
                    continue
                grid[x][y] = path + 1
                toVisit.append(((x,y), path + 1))
            
