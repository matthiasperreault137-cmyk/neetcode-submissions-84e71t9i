class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0

        def DFS(node):
            if grid[node[0]][node[1]] == "0" or node in seen:
                return
            neighbors = [(1, 0), (-1,0), (0,1), (0, -1)]
            seen.add(node)
            for neighbor in neighbors:
                x = node[0] + neighbor[0]
                y = node[1] + neighbor[1]
                if x > len(grid) - 1 or x < 0 or y > len(grid[x]) - 1 or y < 0:
                    continue
                newNode = grid[x][y]
                DFS((x,y))
            return
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                node = grid[i][j]
                print("i" + str(i) + "j" + str(j))
                if node == "0" or (i,j) in seen:
                    continue
                else:
                    DFS((i,j))
                    print("added")
                    islands += 1
        return islands