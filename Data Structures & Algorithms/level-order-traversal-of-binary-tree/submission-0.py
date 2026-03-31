# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        order = deque([root])
        result = []
        level = 1
        ammount = 0
        while order:
            stack = []
            for i in range(level):
                cur = order.popleft()
                stack.append(cur.val)
                if cur.left is not None:
                    order.append(cur.left)
                    ammount += 1
                if cur.right is not None:
                    order.append(cur.right)
                    ammount += 1
            level = ammount
            ammount = 0
            result.append(stack)
        return result