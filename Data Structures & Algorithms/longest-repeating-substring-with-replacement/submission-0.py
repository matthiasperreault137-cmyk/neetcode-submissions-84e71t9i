class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            occurences = {}
            maxocc = 0
            for j in range(i, len(s)):
                occurences[s[j]] = 1 + occurences.get(s[j], 0)
                maxocc = max(maxocc, occurences[s[j]])
                if ((j - i) + 1) - maxocc <= k:
                    res = max(res, j - i + 1)
        return res

    