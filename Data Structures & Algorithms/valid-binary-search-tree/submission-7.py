# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        curr = root
        prev = None

        while stack or curr:
            # go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # process the node
            curr = stack.pop()
            if prev is not None and curr.val <= prev:
                return False
            prev = curr.val

            # move to the right subtree
            curr = curr.right

        return True