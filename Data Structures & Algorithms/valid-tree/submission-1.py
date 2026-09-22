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

        def DFS(node, path, parent):
            if node in path:
                return False
            if node in seen or node not in mapping:
                seen.add(node)
                return True
            path.add(node)
            seen.add(node)
            neighbors = mapping[node]
            print("ts passed" + str(node))
            for neighbor in neighbors:
                print("calling DFS on " + str(neighbor))
                if neighbor == parent:
                    continue
                if not DFS(neighbor, path, node):
                    return False
            path.remove(node)
            return True
        if not DFS(0, set(), None):
            return False
        for i in range(n):
            if i not in seen:
                return False
        return True

    
        