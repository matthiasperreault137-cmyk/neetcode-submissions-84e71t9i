# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        seen = deque()
        seen.append(root)
        tree = []
        visited = set()
        while seen:
            cur = seen.popleft()
            if cur in visited:
                continue
            if cur == None:
                tree.append("null")
                continue
            else:
                tree.append(cur.val)
            visited.add(cur)
            if not cur.left:
                seen.append(None)
            else:
                seen.append(cur.left)
            if not cur.right:
                seen.append(None)
            else:
                seen.append(cur.right)
        return ",".join(map(str, tree))


        

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree = data.split(",")
        cur = None
        parents = deque()
        finalTree = []
        i = 1
        if tree[0] == "null":
            return None
        parents.append(TreeNode(int(tree[0])))
        while parents:
            cur = parents.popleft()
            finalTree.append(cur)
            if cur == None:
                continue
            leftVal = tree[i]
            rightVal = tree[i + 1]
            i += 2
            left = None
            right = None
            if leftVal == "null":
                left = None
            else:
                left = TreeNode(int(leftVal), None, None)
            if rightVal == "null":
                right = None
            else:
                right = TreeNode(int(rightVal), None, None)
            cur.left = left
            cur.right = right
            parents.append(left)
            parents.append(right)
        return finalTree[0]
            


