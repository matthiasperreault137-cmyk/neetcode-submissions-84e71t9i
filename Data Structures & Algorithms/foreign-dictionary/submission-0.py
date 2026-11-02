class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        nodeMap = {}
        for word in words:
            for char in word:
                nodeMap[char] = 0
        last = None
        edges = []
        for word in words:
            if last == None:
                last = word
                continue
            for j in range(min(len(word), len(last))):
                if word[j] != last[j]:
                    edges.append((last[j], word[j]))
                    break
            else:
                if len(word) < len (last):
                    return ""  
            last = word
        changed = True
        while changed:
            changed = False

            for edge in edges:
                a = edge[0]
                b = edge[1]
                if nodeMap[b] < nodeMap[a] + 1:
                    nodeMap[b] = nodeMap[a] + 1
                    if nodeMap[b] >= len(nodeMap):
                        return ""
                    changed = True
        temp = []
        for node, val in nodeMap.items():
            temp.append((node, val))
        temp.sort(key=lambda  x: x[1])
        result = ""
        for bruh in temp:
            result += bruh[0]
        return result