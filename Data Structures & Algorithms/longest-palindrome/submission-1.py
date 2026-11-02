class Solution:
    def longestPalindrome(self, s: str) -> int:
        fuckyou = {}
        for char in s:
            if char in fuckyou:
                fuckyou[char] += 1
            else:
                fuckyou[char] = 1
        

        length = 0
        hasOdd = False

        for val in fuckyou.values():
            if val % 2 == 0:
                length += val
            else:
                if not hasOdd:
                    hasOdd = True
                    length += val
                    continue
                length += val -1
        return length