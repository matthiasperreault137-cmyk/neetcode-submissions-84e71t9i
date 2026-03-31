class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            g = guess(mid)

            if g == 0:
                return mid
            elif g == -1:
                right = mid - 1
            else:
                left = mid + 1
