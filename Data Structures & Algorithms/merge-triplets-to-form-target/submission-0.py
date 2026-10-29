class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0,0,0]

        for triplet in triplets:
            if cur == target:
                return True
            keep = True
            for i in range(len(triplet)):
                if triplet[i] > target[i]:
                    keep = False
                    break
            if keep:
                for i in range(len(cur)):
                    cur[i] = max(cur[i], triplet[i])
        return cur == target