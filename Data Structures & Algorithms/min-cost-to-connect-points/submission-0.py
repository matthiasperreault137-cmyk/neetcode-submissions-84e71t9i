class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parents =  []
        for i in range(len(points)):
            parents.append(i)
        rank = [0] * len(points)
        
        def find(x):
            parent = parents[x]
            if parent != x:
                parents[x] = find(parents[x])
            return parents[x]
        def union(a,b):
            rootA = find(a)
            rootB = find(b)
            sizeA = rank[rootA]
            sizeB = rank[rootB]
            if rootA == rootB:
                return False
            if sizeA > sizeB:
                parents[rootB] = rootA
            elif sizeB > sizeA:
                parents[rootA] = rootB
            else:
                parents[rootB] = rootA
                rank[rootA] += 1
            return True

        edges = []
        for i in range(len(points)):
            p1 = points[i]
            for j in range(i + 1, len(points)):
                p2 = points[j]
                cost = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
                edges.append((cost,i, j))
        edges.sort(key=lambda x: x[0])
        total = 0
        for edge in edges:
            p1 = edge[1]
            p2 = edge[2]
            result = union(p1,p2)
            if result:
                total += edge[0]
        return total
