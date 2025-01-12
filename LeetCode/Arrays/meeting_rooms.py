"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        if not intervals:
            return True
        intervals.sort(key = lambda x:x.start)
        c_end = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < c_end:
                return False
            else:
                c_end = interval.end
        return True
