class Node:
    def __init__(self, children, end):
        if not children:
            self.children = {}
        else:
            self.children = children
        self.end = end
    def addChild(self, character, end):
        node = Node(None, end)
        self.children[character] = node
class WordDictionary:
    def __init__(self):
        self.root = Node(None, False)

    def addWord(self, word: str) -> None:
        cur = self.root
        n = len(word)
        for i in range(n):
            char = word[i]
            if char in cur.children:
                node = cur.children[char]
                if i == n - 1:
                    node.end = True
                cur = node
            else:
                if i == n - 1:
                    cur.addChild(char, True)
                else:
                    cur.addChild(char, False)
                cur = cur.children[char]

    def search(self, word: str) -> bool:
        n = len(word)
        def recurse(node, i, word):
            if node is None:
                return False
            char = word[i + 1]


            if i + 1 == n - 1:
                if char == ".":
                    for kidNode in node.children.values():
                        if kidNode.end == True:
                            return True
                    return False
                else:
                    if char in node.children:
                        kidNode = node.children[char]
                    else:
                        kidNode = None
                    if not kidNode:
                        return False
                    if not kidNode.end:
                        return False
                    return True
            else:
                if char == ".":
                    for kidNode in node.children.values():
                        if recurse(kidNode, i + 1, word):
                            return True
                    return False
                else:
                    if char in node.children:
                        nextNode = node.children[char]
                    else:
                        nextNode = None
                    return recurse(nextNode, i + 1, word)
            return True
        node = self.root
        i = -1
        return recurse(node, i ,word)