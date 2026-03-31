class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        left = 0
        right = 0
        substring = set()
        while right < len(s):
            if s[right] not in substring:
                substring.add(s[right])
                right += 1
                if len(substring) > n:
                    n = len(substring)
            else:
                while s[right] in substring:
                    substring.remove(s[left])
                    left += 1
        return n