class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def quicksort(arr, left, right):
            if left >= right:
                return
            p = hoare(arr, left, right)
            quicksort(arr, left, p)
            quicksort(arr, p + 1, right)
        def hoare(arr, left, right):
            index = median(arr, left, right)
            pivot = arr[index]
            i = left - 1
            j = right + 1
            while True:

                i += 1
                while arr[i] < pivot:
                    i += 1
                j -= 1
                while arr[j] > pivot:
                    j -= 1
                if i >= j:
                    return j
                arr[i], arr[j] = arr[j], arr[i]
        def median(arr, left, right):
            a = arr[left]
            b = arr[(left + right) // 2]
            c = arr[right]
            if a < b:
                if b < c:
                    return (left + right) // 2 
                elif c < a:
                    return left
                else:
                    return right
            else:
                if a < c:
                    return left
                elif c < b:
                    return (left + right) // 2
                else:
                    return right
        n = len(position)
        hashmap = {}
        fleets = 0
        for i in range(n):
            hashmap[position[i]] = speed[i]
        quicksort(position, 0, n - 1)
        for i in range(n):
            distance = target - position[n-i - 1]
            time = distance / hashmap[position[n- i - 1]]
            if fleets != 0 and time <= last:
                continue
            else:
                fleets += 1
                last = time
        return fleets