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
        return self.heap[0]
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = MinHeap(nums)
        self.size = k
        while len(self.heap.heap) > k:
            self.heap.pop()

    def add(self, val: int) -> int:
        if len(self.heap.heap) < self.size:
            self.heap.push(val)
            return self.heap.peek()
        k = self.heap.peek()
        if k >= val:
            return k
        else:
            self.heap.pop()
            self.heap.push(val)
            return self.heap.peek()