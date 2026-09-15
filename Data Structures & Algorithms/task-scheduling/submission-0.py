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
        if not self.heap:
            return None
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
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Creating heap structure
        temp = {}
        for task in tasks:
            if task in temp:
                temp[task] += 1
            else:
                temp[task] = 1
        count = []
        for val in temp.values():
            count.append(val)
        heap = MaxHeap(count)

        time = 0
        queue = deque()
        while heap.heap or queue:
            time += 1
            if queue and queue[0][1] <= time:
                val = queue.popleft()[0]
                heap.push(val)
            if heap.heap:
                val = heap.pop()
                val -= 1
                if val > 0:
                    queue.append((val, time + n + 1))
        return time
                


        