class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def add(self, parent,  node):
        parentR = self.find(parent)
        nodeR = self.find(node)
        if parentR == nodeR:
            return
        if self.rank[parentR] < self.rank[nodeR]:
            parentR, nodeR = nodeR, parentR
        self.parent[nodeR] = parentR
        if self.rank[nodeR] == self.rank[parentR]:
            self.rank[parentR] += 1
        return

        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for i in range(len(edges)):
            edge = edges[i]
            dsu.add(edge[0], edge[1])
        results = set()
        total = 0
        for i in range(n):
            val = dsu.find(i)
            if val not in results:
                results.add(val)
                total += 1
        return total
            
                