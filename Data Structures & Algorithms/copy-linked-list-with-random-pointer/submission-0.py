"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodemap = {}
        def copyN(head):
            if head is None:
                return None
            copy = Node(head.val)
            nodemap[head] = copy
            copy.next = copyN(head.next)
            if head.random is None:
                copy.random = None
            else:
                copy.random = nodemap[head.random]
            return copy
        return copyN(head)