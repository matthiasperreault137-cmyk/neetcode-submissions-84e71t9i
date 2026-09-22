class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        mapping = {}
        for i in range(len(edges)):
            if edges[i][0] not in mapping:
                mapping[edges[i][0]] = []
            mapping[edges[i][0]].append(edges[i][1])
            if edges[i][1] not in mapping:
                mapping[edges[i][1]] = []
            mapping[edges[i][1]].append(edges[i][0])

        toVisit = deque()
        toVisit.append((0, None))
        seen.add(0)
        while toVisit:
            popVal = toVisit.popleft()
            val = popVal[0]
            parent = popVal[1]
            if val not in mapping:
                continue
            neighbors = mapping[val]
            for neighbor in neighbors:
                if neighbor == parent:
                    continue
                if neighbor in seen:
                    return False
                seen.add(neighbor)
                toVisit.append((neighbor, val))
        for i in range(n):
            if i not in seen:
                return False
        return True

        