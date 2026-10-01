class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def Check(i):
            if i in dp:
                if dp[i]:
                    return True
                else:
                    return False
            string = ""
            for j in range(i, len(s)):
                string += s[j]
                for word in wordDict:
                    if word == string:
                        if Check(i + len(word)):
                            dp[i] = True
                            return True
            dp[i] = False
            return False

        dp[len(s)] = True
        for i in range(len(s) - 1, 0, -1):
            Check(i)
        return Check(0)