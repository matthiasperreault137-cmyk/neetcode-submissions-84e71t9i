import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, x):
        start, end = x
        heapq.heappush(self.heap, (end - start + 1, start, end))

    def pop(self):
        _, start, end = heapq.heappop(self.heap)
        return (start, end)

    def peek(self):
        _, start, end = self.heap[0]
        return (start, end)

    def __len__(self):
        return len(self.heap)


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x : x[0])

        i = 0
        heap = MinHeap()
        results = {}
        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                heap.push(intervals[i])
                i += 1
            while heap.heap and heap.peek()[1] < query:
                heap.pop()
            if not heap.heap:
                results[query] = -1
                continue
            else:
                results[query] = heap.peek()[1] - heap.peek()[0] + 1
        return [results[query] for query in queries]

















