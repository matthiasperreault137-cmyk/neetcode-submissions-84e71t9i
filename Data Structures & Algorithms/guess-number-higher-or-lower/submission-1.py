# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i = 0
        j = n
        mid = None
        while i <= j:
            mid = (i + j) // 2
            midVal = guess(mid)
            if midVal == 0:
                return mid
            elif midVal == -1:
                j = mid
                j -= 1
            else:
                i = mid
                i += 1
        return mid
         