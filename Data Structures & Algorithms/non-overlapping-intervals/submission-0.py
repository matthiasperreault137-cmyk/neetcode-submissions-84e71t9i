class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        results = []
        result = 0
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals)):
            cur = intervals[i]
            if not results:
                results.append(cur)
                continue
            last = results[-1]
            if cur[0] >= last[1]:
                results.append(cur)
            else:
                if cur[1] < last[1]:
                    results.pop()
                    results.append(cur)
                result += 1
        print(len(results))
        return result
            