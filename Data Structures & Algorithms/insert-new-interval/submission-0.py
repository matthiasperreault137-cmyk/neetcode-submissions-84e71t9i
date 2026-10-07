class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        start, end = newInterval
        i = 0

        # skip intervals that end before the new one starts
        while i < n and intervals[i][1] < start:
            i += 1
        a = i

        # merge every interval that overlaps the new one
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        return intervals[:a] + [[start, end]] + intervals[i:]