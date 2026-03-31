# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        head = root
        if root is None:
            node = TreeNode(val)
            return node
        while True:
            if root.val > val and root.left is not None:
                root = root.left
            elif root.val < val and root.right is not None:
                root = root.right
            elif root.val > val and root.left is None:
                node = TreeNode(val)
                root.left = node
                break
            else:
                node = TreeNode(val)
                root.right = node
                break
        return head
