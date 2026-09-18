class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Atlantic = set()
        Pacific = set()
        Touching = set()
        neighbors = [(1,0), (-1,0), (0, 1), (0,-1)]
        results = []
        def addOcean(pos, ocean):
            if ocean == 1:
                Atlantic.add(pos)
            else:
                Pacific.add(pos)
        def checkOcean(pos,ocean):
            if ocean == 1:
                if pos in Atlantic:
                    return True
                else:
                    return False
            else:
                if pos in Pacific:
                    return True
                else:
                    return False
             
        def DFS(position, ocean):
            
            toVisit = []
            toVisit.append(position)
            addOcean(position, ocean)
            while toVisit:
                pos = toVisit.pop()
                height = heights[pos[0]][pos[1]]
                for neighbor in neighbors:
                    x = pos[0] + neighbor[0]
                    y = pos[1] + neighbor[1]
                    if x < 0 or y < 0 or x > len(heights) - 1 or y > len(heights[x]) - 1:
                        continue
                    neighbourHeight = heights[x][y]
                    if height > neighbourHeight:
                        continue
                    if checkOcean((x,y), ocean):
                        continue
                    addOcean((x,y), ocean)
                    toVisit.append((x,y))
            return
        for i in range(len(heights[0])):
            DFS((0,i), 2)
            DFS((len(heights) - 1, i), 1)
        for j in range(len(heights)):
            DFS((j, 0), 2)
            DFS((j, len(heights[j]) - 1), 1)

        for a in range(len(heights)):
            for b in range(len(heights[a])):
                if checkOcean((a,b), 1) and checkOcean((a,b), 2):
                    results.append([a,b])
        return results
                    
                    


                    