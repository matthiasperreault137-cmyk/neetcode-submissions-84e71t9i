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
class PrefixTree:

    def __init__(self):
        self.root = Node(None, False)

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            if char in cur.children:
                node = cur.children[char]
                if i == len(word) - 1:
                    node.end = True
                cur = node
            else:
                if i == len(word) - 1:
                    cur.addChild(char, True)
                else:
                    cur.addChild(char, False)
                cur = cur.children[char]

    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in cur.children:
                return False
            cur = cur.children[char]
            if i == len(word) - 1:
                if cur.end == False:
                    return False
        return True
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
        