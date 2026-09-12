class MaxHeap:
    def __init__(self, array=None):
        self.heap = self.heapifyAll(array if array is not None else [])

    def push(self, item):
        self.heap.append(item)
        i = len(self.heap) - 1

        while i > 0:
            p = (i - 1) // 2
            if self.heap[i][0] > self.heap[p][0]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    def pop(self):
        num = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self.heapifyDown(0, self.heap)
        return num

    def heapifyDown(self, i, array):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < len(array) and array[left][0] > array[largest][0]:
            largest = left
        if right < len(array) and array[right][0] > array[largest][0]:
            largest = right
        if largest == i:
            return
        array[i], array[largest] = array[largest], array[i]
        self.heapifyDown(largest, array)

    def heapifyAll(self, array):
        copy = array.copy()
        cutoff = (len(copy) // 2) - 1
        for i in range(cutoff, -1, -1):
            self.heapifyDown(i, copy)
        return copy

    def peek(self):
        return self.heap[0]

    def __len__(self):
        return len(self.heap)


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = MaxHeap()

        for point in points:
            x, y = point[0], point[1]
            distance = x ** 2 + y ** 2  # no need for sqrt, just comparing
            heap.push((distance, point))
            if len(heap) > k:
                heap.pop()

        return [item[1] for item in heap.heap]