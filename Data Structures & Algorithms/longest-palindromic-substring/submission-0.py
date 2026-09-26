class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return 0
        maxlen = 0
        maxinds = [None, None]
        for i in range(len(s)):
            #fuckass problem
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left) + 1 > maxlen:
                    maxinds[0] = left
                    maxinds[1] = right
                    maxlen = (right - left + 1)
                left -= 1
                right += 1
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left) + 1 > maxlen:
                    maxinds[0] = left
                    maxinds[1] = right
                    maxlen = (right - left + 1)
                left -= 1
                right += 1
        if maxlen == 1:
            return s[0]
        else:
            result = ""
            for i in range(maxinds[0], maxinds[1] + 1):
                char = s[i]
                result += char
            return result
