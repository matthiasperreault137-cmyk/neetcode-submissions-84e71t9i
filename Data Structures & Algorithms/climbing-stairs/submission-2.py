class Solution:
    def climbStairs(self, n: int) -> int:
        temp1 = 1
        temp2 = 1
        total = 0
        if n <= 1:
            return 1
        for i in range(n - 1):
            total = temp1 + temp2
            temp1 = temp2
            temp2 = total  
        return total