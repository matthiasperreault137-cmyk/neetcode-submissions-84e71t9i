# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def dfs(root):
            if root is None:
                return 0
            return 1 + max(dfs(root.left), dfs(root.right))
        left = dfs(root.left)
        right = dfs(root.right)
        if not self.isBalanced(root.right) or not self.isBalanced(root.left):
            return False
        if left == right or right == left - 1 or left == right - 1:
            return True
        return False
        