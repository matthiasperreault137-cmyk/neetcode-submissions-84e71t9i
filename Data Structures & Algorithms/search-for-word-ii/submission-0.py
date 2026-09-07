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


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node(None, None)

        def addWord(word: str) -> None:
            cur = root
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

        for word in words:
            addWord(word)

        tempWords = set()
        path = set()

        def DFS(node, gridSlot, wordChars):
            if node.end:
                tempWords.add("".join(wordChars))

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newRow = gridSlot[0] + dr
                newCol = gridSlot[1] + dc
                gridSlotNew = (newRow, newCol)

                if 0 <= newRow < len(board) and 0 <= newCol < len(board[0]) and gridSlotNew not in path:
                    nextChar = board[newRow][newCol]
                    if nextChar in node.children:
                        kidNode = node.children[nextChar]
                        path.add(gridSlotNew)
                        wordChars.append(nextChar)
                        DFS(kidNode, gridSlotNew, wordChars)
                        wordChars.pop()
                        path.remove(gridSlotNew)

        for i in range(len(board)):
            for j in range(len(board[i])):
                char = board[i][j]
                if char in root.children:
                    node = root.children[char]
                    path.add((i, j))
                    DFS(node, (i, j), [char])
                    path.remove((i, j))

        return list(tempWords)