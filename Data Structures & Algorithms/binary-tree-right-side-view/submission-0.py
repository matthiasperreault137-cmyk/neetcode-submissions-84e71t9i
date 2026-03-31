# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None :
            return []
        order = deque([root])
        results = []
        level = 1
        ammount = 0
        while order:
            for i in range(level):
                cur = order.popleft()
                if cur.left is not None:
                    order.append(cur.left)
                    ammount += 1
                if cur.right is not None:
                    order.append(cur.right)
                    ammount += 1
                if i == level - 1:
                    results.append(cur.val)
            level = ammount
            ammount = 0
        return results            