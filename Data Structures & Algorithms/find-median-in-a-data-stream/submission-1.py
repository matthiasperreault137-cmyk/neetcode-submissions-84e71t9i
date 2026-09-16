class MinHeap:
    def __init__(self, array):
        self.heap = self.heapifyAll(array)

    def push(self, num):
        self.heap.append(num)
        i = len(self.heap) - 1

        while i > 0:
            p = (i - 1) // 2
            if self.heap[i] < self.heap[p]:
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

        smallest = i

        if left < len(array) and array[left] < array[smallest]:
            smallest = left
        if right < len(array) and array[right] < array[smallest]:
            smallest = right
        if smallest == i:
            return
        temp = array[i]
        array[i] = array[smallest]
        array[smallest] = temp
        self.heapifyDown(smallest, array)
        return

    def heapifyAll(self, array):
        copy = array.copy()
        cutoff = (len(copy) // 2) - 1
        for i in range(cutoff, -1, -1):
            self.heapifyDown(i, copy)
        return copy
    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]
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
        if not self.heap:
            return None
        return self.heap[0]

class MedianFinder:

    def __init__(self):
        self.minHeap = MinHeap([])
        self.maxHeap = MaxHeap([])
        self.minTotal = 0
        self.maxTotal = 0

    def addNum(self, num: int) -> None:
        minMedianVal = self.maxHeap.peek()
        maxMedianVal = self.minHeap.peek()

        if not minMedianVal or num >= minMedianVal:
            if self.maxTotal < self.minTotal:
                self.minHeap.push(num)
                overFlow = self.minHeap.pop()
                self.maxHeap.push(overFlow)
                self.maxTotal += 1
            else:
                self.minHeap.push(num)
                self.minTotal += 1
        else:
            if self.maxTotal > self.minTotal:
                self.maxHeap.push(num)
                overFlow = self.maxHeap.pop()
                self.minHeap.push(overFlow)
                self.minTotal += 1
            else:
                self.maxHeap.push(num)
                self.maxTotal += 1


    def findMedian(self) -> float:
        total = self.maxTotal + self.minTotal
        if total % 2 == 1:
            if self.maxTotal > self.minTotal:
                return self.maxHeap.peek()
            else:
                return self.minHeap.peek()
        else:
            minVal = self.minHeap.peek()
            maxVal = self.maxHeap.peek()
            median = (minVal + maxVal) / 2
            return median

        