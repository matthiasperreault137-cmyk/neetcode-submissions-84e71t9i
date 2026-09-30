class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        Vals = {}
        Vals[0] = 0
        if amount == 0:
            return 0
        for i in range(1, amount + 1):
            best = 1e9
            for coin in coins:
                if i - coin < 0:
                    continue
                if Vals[i - coin] == -1:
                    continue
                else:
                    best = min(best, Vals[i - coin])
            if best >= 1e9:
                Vals[i] = -1
            else:
                Vals[i] = best + 1
        return Vals[amount]
