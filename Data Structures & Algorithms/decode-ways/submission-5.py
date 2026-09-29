class Solution:
    def numDecodings(self, s: str) -> int:
        ValMap = {}
        def Count(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in ValMap:
                return ValMap[i]
            total = Count(i + 1)
            if i + 1 < len(s) and int(s[i] + s[i + 1]) <= 26:
                total += Count(i + 2)
            ValMap[i] = total
            return total
        return Count(0)