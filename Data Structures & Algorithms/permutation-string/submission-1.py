class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        substring = {}
        window = {}
        ss = ""
        bs = ""
        if len(s1) > len(s2):
            ss += s2
            bs += s1
            return False
        else:
            ss += s1
            bs += s2
        for i in range(len(ss)):
            substring[ss[i]] = 1 + substring.get(ss[i], 0)
        left = 0
        for right in range(len(bs)):
            window[bs[right]] = 1 + window.get(bs[right], 0)
            if right - left + 1 > len(ss):
                window[bs[left]] -= 1
                if window[bs[left]] == 0:
                    del window[bs[left]]
                left += 1
            if window == substring:
                return True
        return False