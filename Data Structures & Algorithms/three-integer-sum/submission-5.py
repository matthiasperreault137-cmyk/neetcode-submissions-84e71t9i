class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def quicksort(arr, left, right):
            if left < right:
                value = median(arr, left, right)
                pivot = partition(arr, value, left, right)
                quicksort(arr, left,  pivot)
                quicksort(arr, pivot + 1, right)
        def partition(arr, pivot, left, right):
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
                arr[i] , arr[j] = arr[j] , arr[i]          
        def median(arr, left, right):
            a = arr[left]
            b = arr[right]
            c = arr[(left + right) // 2]
            if a > b:
                if b > c:
                    return b
                elif a > c:
                    return c
                else:
                    return a
            else:
                if a > c:
                    return a
                elif b > c:
                    return c
                else:
                    return b
        quicksort(nums, 0 ,len(nums) - 1)
        stack = []
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            knum = -nums[k]
            i = k + 1
            j = len(nums) - 1
            while i < j:
                num = nums[i] + nums[j]
                if knum - num == 0:
                    stack.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while  i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif knum - num < 0:
                    j -= 1
                else:
                    i += 1
        return stack