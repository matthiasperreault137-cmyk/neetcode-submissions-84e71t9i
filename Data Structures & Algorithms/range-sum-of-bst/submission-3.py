# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            total = 0
            if node.val < low:
                total += dfs(node.right)
                return 0 + total
            elif node.val > high:
                total += dfs(node.left)
                return 0 + total
            else:
                total = dfs(node.left) + dfs(node.right)
            print(node.val)
            total += node.val
            return total
        return dfs(root)

