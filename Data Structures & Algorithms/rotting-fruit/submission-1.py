class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        neighbors = [(1,0), (-1,0), (0,1), (0,-1)]
        toVisit = deque()
        timeVals = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                val = grid[i][j]
                if val == 2:
                    toVisit.append(((i, j), 0))
        
        while toVisit:
            popVal = toVisit.popleft()
            pos = popVal[0]
            time = popVal[1]

            for neighbor in neighbors:
                x = pos[0] + neighbor[0]
                y = pos[1] + neighbor[1]

                if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[x]) - 1:
                    continue
                val = grid[x][y]
                timeVal = 10000000
                if (x,y) in timeVals:
                    timeVal = timeVals[(x,y)]
                if val == 0 or val == 2 or timeVal <= time + 1:
                    continue
                print("exploring x" + str(x) + "y" + str(y))
                print(str(time + 1))
                timeVals[(x,y)] = time + 1
                toVisit.append(((x,y), time + 1))
        maxVal = -10000000
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                cell = grid[i][j]
                if cell == 1:
                    if (i,j) not in timeVals:
                        return -1
                    else:
                        print(timeVals[(i,j)])
                        maxVal = max(timeVals[(i,j)], maxVal)
        if maxVal <= -100000:
            return 0
        else:
            return maxVal  