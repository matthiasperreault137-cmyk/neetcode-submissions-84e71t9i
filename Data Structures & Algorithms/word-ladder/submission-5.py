class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        tried = {}
        seen = set()
        def DFS(word):
            if word == endWord:
                return 1
            if word in seen:
                return 0
            if word in tried:
                return tried[word]
            best = None
            seen.add(word)
            for w in wordList:
                repI = None
                for i in range(len(word)):
                    if word[i] != w[i]:
                        if repI != None:
                            repI = None
                            break
                        repI = i
                if repI == None:
                    continue
                temp = word[repI]
                word = word[:repI] + w[repI] + word[repI + 1:]
                val = DFS(word)
                if val != 0:
                    if best == None:
                        best = val
                    else:
                        best = min(best, val)
                word = word[:repI] + temp + word[repI + 1:]
            seen.remove(word)
            if best == None:
                tried[word] = 0
                return 0
            tried[word] = best + 1
            return best + 1
        result = 0
        return DFS(beginWord)


            

                         

