"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def merge_sort(intervals):
            if len(intervals) <= 1:
                return intervals

            mid = len(intervals) // 2
            left = merge_sort(intervals[:mid])
            right = merge_sort(intervals[mid:])

            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i].start <= right[j].start:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        intervals = merge_sort(intervals)
        last_end = float('-inf')
        for interval in intervals:
            if interval.start < last_end:
                return False
            last_end = interval.end
        return True