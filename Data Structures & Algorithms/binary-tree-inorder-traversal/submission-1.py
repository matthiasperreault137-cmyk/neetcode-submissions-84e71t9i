# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        result = []
        cur = root
        while cur or order:
            while cur:
                order.append(cur)
                cur = cur.left
            cur = order.pop()
            result.append(cur.val)
            cur = cur.right
        return result
