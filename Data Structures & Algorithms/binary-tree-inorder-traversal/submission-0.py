# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        def traverss(root):
            if root is None:
                return
            traverss(root.left)
            stack.append(root.val)
            traverss(root.right)
            return
        traverss(root)
        return stack