class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        results = []
        for i in range(len(nums)):
            num = nums[i]
            hashmap[num] = 1 + hashmap.get(num, 0)
        bucket = {}
        for i in range(len(nums) + 1):
            bucket[i] = []
        for num in hashmap:
            bucket[hashmap[num]].append(num)
        n = len(nums)
        while k > 0:
            while not bucket[n]:
                n -= 1
            results.extend(bucket[n])
            k -= len(bucket[n])
            n -= 1
        return results