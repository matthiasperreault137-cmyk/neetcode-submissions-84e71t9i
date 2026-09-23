class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        mapping = {}
        temp = wordList.copy()
        temp.append(beginWord)
        for word in temp:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                if key not in mapping:
                    mapping[key] = []
                mapping[key].append(word)

        toVisit = deque()
        toVisit.append((beginWord, 1))
        seen = set()
        seen.add(beginWord)
        while toVisit:
            popVal = toVisit.popleft()
            word = popVal[0]
            val = popVal[1]
            print(word + "popped")
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                print("key : " + key)
                neighbors = mapping[key]
                for neighbor in neighbors:
                    if neighbor == endWord:
                        return val + 1
                    if neighbor in seen:
                        continue
                    seen.add(neighbor)
                    toVisit.append((neighbor, val + 1))
        return 0
        
