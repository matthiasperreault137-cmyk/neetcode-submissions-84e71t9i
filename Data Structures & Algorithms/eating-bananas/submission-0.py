class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxB = 0
        for i in range(len(piles)):
            if piles[i] > maxB:
                maxB = piles[i]
        i = 1
        j = maxB
        hunger = None
        while i <= j:
            mid = (i + j) // 2
            hours = self.hours(piles, mid)
            if hours <= h:
                j = mid - 1
                hunger = mid
            else:
                i = mid + 1
        return hunger
    def hours(self, bananas, hunger):
        hours = 0
        for i in range(len(bananas)):
            hours += (bananas[i] + hunger - 1) // hunger
        return hours