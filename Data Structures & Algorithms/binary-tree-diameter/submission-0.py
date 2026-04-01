# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        globalmax = 0
        def dfs(root):
            nonlocal globalmax
            if root is None:
                return 0
            else:
                leftheight = dfs(root.left)
                rightheight = dfs(root.right)
                globalmax = max(globalmax, leftheight + rightheight)
                return 1 + max(leftheight,rightheight)
        dfs(root)
        return globalmax