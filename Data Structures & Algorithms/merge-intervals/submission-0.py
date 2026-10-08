class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        results = []
        i = 1
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1 , len(intervals)):
            cur = intervals[i]
            if end >= cur[0]:
                if cur[1] > end:
                    end = cur[1]
            else:
                results.append([start,end])
                start = cur[0]
                end = cur[1]
        results.append([start, end])
        return results
