class MaxHeap:
    def __init__(self, array):
        self.heap = self.heapifyAll(array)

    def push(self, num):
        self.heap.append(num)
        i = len(self.heap) - 1

        while i > 0:
            p = (i - 1) // 2
            if self.heap[i] > self.heap[p]:
                temp = self.heap[i]
                self.heap[i] = self.heap[p]
                self.heap[p] = temp
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

        if left < len(array) and array[left] > array[largest]:
            largest = left
        if right < len(array) and array[right] > array[largest]:
            largest = right
        if largest == i:
            return
        temp = array[i]
        array[i] = array[largest]
        array[largest] = temp
        self.heapifyDown(largest, array)
        return

    def heapifyAll(self, array):
        copy = array.copy()
        cutoff = (len(copy) // 2) - 1
        for i in range(cutoff, -1, -1):
            self.heapifyDown(i, copy)
        return copy

    def peek(self):
        return self.heap[0]
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MaxHeap(stones)
        while len(heap.heap) > 1:
            x = heap.pop()
            y = heap.pop()
            z = x - y
            if z != 0:
                heap.push(z)
        if len(heap.heap) == 0:
            return 0
        return heap.pop()

