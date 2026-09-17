"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        visited = set()
        nodeMap = {}
        toVisit = [node]
        nodeMap[node] = Node(node.val)
        visited.add(node)
        while toVisit:
            cur = toVisit.pop()
            copy = nodeMap[cur]
            for neighbor in cur.neighbors:
                neighborCopy = None
                if neighbor in nodeMap:
                    neighborCopy = nodeMap[neighbor]
                else:
                    neighborCopy = Node(neighbor.val)
                    nodeMap[neighbor] = neighborCopy
                copy.neighbors.append(neighborCopy)
                if neighbor in visited:
                    continue
                else:

                    visited.add(neighbor)
                    toVisit.append(neighbor)
        return nodeMap[node]