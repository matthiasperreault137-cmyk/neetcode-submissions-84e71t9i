# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if root is None and subroot is None:
            return True
        elif root is None:
            return False
        elif subroot is None:
            return True
        else:
            def equal(root, subroot):
                if root is None and subroot is None:
                    return True
                elif root and subroot:
                    if root.val == subroot.val:
                        return equal(root.left, subroot.left) and equal(root.right, subroot.right)
                else:
                    return False
            if self.isSubtree(root.right, subroot) or self.isSubtree(root.left, subroot) or equal(root,subroot):
                return True
            else:
                return False