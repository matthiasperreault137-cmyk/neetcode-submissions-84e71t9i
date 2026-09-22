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
        mapping = {}
        for i in range(len(edges)):
            if edges[i][0] not in mapping:
                mapping[edges[i][0]] = []
            mapping[edges[i][0]].append(edges[i][1])
    #        if edges[i][1] not in mapping:
     #           mapping[edges[i][1]] = []
      #          mapping[edges[i][1]].append(edges[i][0])

        dsu = DSU(n)

        seen = set()
        for i in range(n):
            if i in seen:
                continue
            seen.add(i)
            if i not in mapping:
                continue
            toVisit = []
            toVisit.append(i)
            while toVisit:
                val = toVisit.pop()
                reqs = mapping[val]
                for req in reqs:
                    dsu.add(val, req)
                    if req in seen:
                        continue
                    seen.add(req)
                    if req not in mapping:
                        continue
                    toVisit.append(req) 
        results = set()
        total = 0
        for i in range(n):
            val = dsu.find(i)
            if val not in results:
                results.add(val)
                total += 1
        return total
            
                