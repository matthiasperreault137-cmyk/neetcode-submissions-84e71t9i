# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = -999999
        def TreeSum(root):
            if not root:
                return 0
            nonlocal maxVal
            leftVal = TreeSum(root.left)
            rightVal = TreeSum(root.right)
            if leftVal < 0:
                leftVal = 0
            if rightVal < 0:
                rightVal = 0
            val = None
            if rightVal >= leftVal:
                val = root.val + rightVal
            else:
                val = root.val + leftVal
            if val > maxVal:
                maxVal = val
            potentialVal = root.val + leftVal + rightVal
            if potentialVal > maxVal:
                maxVal = potentialVal
            return val
        TreeSum(root)
        return maxVal
