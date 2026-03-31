class Solution:
    def minWindow(self, s: str, t: str) -> str:
        contain = False
        substring = {}
        frequencies = {}
        truth = {}
        minlen = len(s)
        pointers = [0, len(s) - 1]
        for i in range(len(t)):
            if t[i] not in substring:
                truth[t[i]] = True
            substring[t[i]] = 1 + substring.get(t[i], 0)
            
        left = 0
        current = {}
        for right in range(len(s)):
            if s[right] in substring:
                current[s[right]] = 1 + current.get(s[right], 0)
                if current[s[right]] >= substring[s[right]]:
                    frequencies[s[right]] = True
                    while left <= right and frequencies == truth:
                        if minlen >= (right - left + 1):
                            minlen = right - left + 1
                            pointers[0] = left
                            pointers[1] = right
                            contain = True
                        if s[left] in substring:
                            current[s[left]] = current.get(s[left]) - 1
                            if current[s[left]] < substring[s[left]]:
                                frequencies[s[left]] = False
                            if current[s[left]] == 0:
                                del current[s[left]]
                        left += 1
            else:
                continue
        result = s[pointers[0]:pointers[1] + 1]
        if not contain:
            return ""
        return result
