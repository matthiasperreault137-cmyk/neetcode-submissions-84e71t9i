class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        dpMap = [None] * n
        for a in range(n):
            row = [0] * n
            dpMap[a] = row

        for i in range(len(s)):
            for j in range(len(s)):
                left = j - i
                if left < 0:
                    continue
                right = j + i
                if right >= len(s):
                    continue
                if i == 0 or (s[left] == s[right] and dpMap[left + 1][right - 1] == 1):
                    count += 1
                    dpMap[left][right] = 1
                right = j + 1 + i
                if right >= len(s):
                    continue
                if (s[left] == s[right]) and (i == 0 or dpMap[left + 1][right - 1] == 1):
                    count += 1
                    dpMap[left][right] = 1
        return count
