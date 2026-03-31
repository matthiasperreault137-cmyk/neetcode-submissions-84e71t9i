class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        occurences = {}
        maxocc = 0
        for right in range(len(s)):
            occurences[s[right]] = 1 + occurences.get(s[right], 0)
            maxocc = max(maxocc, occurences[s[right]])
            while ((right - left) + 1) - maxocc > k:
                occurences[s[left]] -= 1
                left += 1
            res = max(res, (right - left) + 1)
        return res