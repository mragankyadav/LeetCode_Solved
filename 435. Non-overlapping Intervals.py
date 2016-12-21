# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals=sorted(intervals,key=lambda s: (s.end))
        count=0
        for i in range(len(intervals)):
            if i==0:
                continue
            if intervals[i].start<intervals[i-1].end:
                count+=1
                
                intervals[i].start=intervals[i-1].start
                intervals[i].end=intervals[i-1].end
        return count