class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        seen = set()
        toVisit = deque()
        toVisit.append((beginWord, 1))
        seen.add(beginWord)
        while toVisit:
            popVal = toVisit.pop()
            word = popVal[0]
            val = popVal[1]
            print("pooped" + word)
            for w in wordList:
                repI = None
                for i in range(len(word)):
                    if word[i] != w[i]:
                        print(word[i] + "char1" + w[i] + "char2")
                        if repI != None:
                            repI = None
                            break
                        repI = i
                if repI == None:
                    print(w + "is invalid")
                    continue
                temp = word[repI]
                word = word[:repI] + w[repI] + word[repI + 1:]
                if word == endWord:
                    return val + 1
                if word not in seen:
                    toVisit.append((word, val + 1))
                    seen.add(word)
                    print(word)
                    word = word[:repI] + temp + word[repI + 1:]
                else:
                    word = word[:repI] + temp + word[repI + 1:]
                    continue
        return 0

            

                         

