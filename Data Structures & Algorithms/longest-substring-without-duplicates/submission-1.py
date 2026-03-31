class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        for i in range(len(s) - 1):
            substring = set()
            substring.add(s[i])
            for j in range(i + 1, len(s)):
                if s[j] not in substring:
                    substring.add(s[j])
                else:break
            if len(substring) > n:
                n = len(substring)
        return n