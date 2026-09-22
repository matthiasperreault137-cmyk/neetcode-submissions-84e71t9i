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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        dsu = DSU(len(edges) + 1)
        
        possibilities = []
        for i in range(len(edges)):
            edge = edges[i]
            val1 = edge[0]
            val2 = edge[1]

            rep1 = dsu.find(val1)
            rep2 = dsu.find(val2)

            if rep1 == rep2:
                possibilities.append(edge)
                continue
            dsu.add(val1, val2)
        if not possibilities:
            return []
        return possibilities[-1] 
