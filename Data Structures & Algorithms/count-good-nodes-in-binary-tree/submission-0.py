# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        valid = []
        def isGood(root, maxVal):
            if not root:
                return 
            if root.val < maxVal:
                isGood(root.left, maxVal)
                isGood(root.right, maxVal)
            else:
                valid.append(root)
                isGood(root.left, root.val)
                isGood(root.right, root.val) 
        if not root:
            return 0
        else:
            valid.append(root)
        isGood(root.left, root.val)
        isGood(root.right, root.val)
        return len(valid)