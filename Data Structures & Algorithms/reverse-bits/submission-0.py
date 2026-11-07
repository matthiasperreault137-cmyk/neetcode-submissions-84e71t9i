class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if res != 0:
                res <<= 1
            val = n % 2
            n >>= 1
            res += val
        return res
