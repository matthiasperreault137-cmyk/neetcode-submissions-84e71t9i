class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        differences = []
        quickCheck = 0
        cur = 0
        total = 0
        for i in range(len(gas)):
            differences.append(gas[i] - cost[i])
        for i in range(len(differences)):
            if total < 0:
                total = 0
                cur = i
            total += differences[i]
            quickCheck += differences[i]
        if quickCheck < 0:
            return -1
        return cur