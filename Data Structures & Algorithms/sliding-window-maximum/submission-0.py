from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        left = 0
        results = []
        for right in range(len(nums)):
            while deq and deq[-1] < nums[right]:
                deq.pop()
            deq.append(nums[right])
            if (right - left) + 1 == k:
                results.append(deq[0])
                left += 1
                if nums[left - 1] == deq[0]:
                    deq.popleft()
        return results