class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        maxprofit = 0
        while j < len(prices):
            right = prices[j]
            left = prices[i]
            profit = right - left
            if profit > maxprofit:
                maxprofit = profit
            if right < left:
                i = j
            j += 1
        return maxprofit