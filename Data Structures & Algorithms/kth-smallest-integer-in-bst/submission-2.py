# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        order = []
        stack = []
        cur = root
        while cur or order:
            while cur:
                order.append(cur)
                cur = cur.left
            cur = order.pop()
            stack.append(cur.val)
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
        return stack[k -1]