class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        def partition(low, high, array):
            if low >= high:
                return array[low]
            i ,j = low, low
            pivot = array[high]
            while j <= high:
                val = array[j]
                if val < pivot:
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
                    i += 1
                    j += 1
                    continue
                j += 1
            temp = array[i]
            array[i] = pivot
            array[high] = temp
            if target == i:
                return array[i]
            elif target < i:
                return partition(low, i - 1, array)
            else:
                return partition(i + 1, high, array)
        return partition(0, len(nums) -1 , nums)