class Solution:
    def climbStairs(self, n: int) -> int:
        cur = 1
        last = 0
        for i in range(n):
            temp = cur
            cur = cur + last
            last = temp
        return cur