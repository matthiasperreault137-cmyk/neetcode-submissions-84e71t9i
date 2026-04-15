# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        set1 = []
        set2 = []
        def dfs(root, setx):
            if root is None:
                setx.append(None)
                return 0
            setx.append(root.val)
            total = dfs(root.left, setx) + dfs(root.right,setx) + root.val
            return total
        dfs(p, set1)
        dfs(q,set2)
        if set1 == set2:
            return True
        else:
            return False
        