class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        counts = {}
        for num in hand:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for i in counts:
            while counts[i] > 0:
                for j in range(i, i + groupSize):
                    if j not in counts or counts[j] == 0:
                        return False
                    else:
                        counts[j] -= 1
        return True

            