"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []

        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()

        j = 0
        rooms = 0
        
        for i in range(len(starts)):
            start = starts[i]
            if start >= ends[j]:
                j += 1
            rooms = max((i + 1 - j), rooms)
        return rooms