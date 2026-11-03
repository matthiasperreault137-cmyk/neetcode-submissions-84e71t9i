import heapq
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = deque()
        result.appendleft(-1)
        i = len(arr) - 2
        maxVal = arr[len(arr) - 1]
        while i >= 0:
            result.appendleft(maxVal)
            num = arr[i]
            maxVal = max(num, maxVal)
            i -= 1
        return list(result)