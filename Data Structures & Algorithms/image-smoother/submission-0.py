class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        newMatrix = []
        for i in range(len(img)):
            newMatrix.append([])
        nbs = [(1,1), (1,0), (1, -1), (0,1),(0,0),(0,-1),(-1,1),(-1,0),(-1,-1)]
        for i in range(len(img)):
            for j in range(len(img[i])):
                total = 0
                count = 0
                for nb in nbs:
                    x = nb[0] + i
                    y = nb[1] + j
                    if x < 0 or y < 0 or x >= len(img) or y >= len(img[x]):
                        continue
                    total += img[x][y]
                    count += 1
                newMatrix[i].append(total // count)
        return newMatrix
                