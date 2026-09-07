"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # input [(0,40),(5,10),(15,20)]
        starts = sorted(i.start for i in intervals) # 0, 5, 15
        ends   = sorted(i.end   for i in intervals) # 10, 20, 40

        res = count = 0
        s = e = 0

        while s < len(intervals):
            if starts[s] < ends[e]: # 0 < 10 then add room
                count += 1
                s  += 1
            else: # start[15] > end[10] remove room  
                count -= 1 
                e += 1
            res = max(res, count)
        
        return res
                