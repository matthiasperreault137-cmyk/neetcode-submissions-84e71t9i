class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        result = []
        i = 0
        seen = set()
        for num in hashset:
            if num - 1 in seen or num in seen:
                continue
            else:
                seen.add(num)
                temp = []
                while num in hashset:
                    seen.add(num)
                    temp.append(num)
                    num += 1
                if len(temp) > len(result):
                    result = temp
        return len(result)