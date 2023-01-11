'''
https://www.lintcode.com/problem/919/
919 · Meeting Rooms II
Algorithms
Medium
Accepted Rate
53%
Description
Solution78
Notes99+
Discuss8
Leaderboard
Record
Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

(0,8),(8,10) is not conflict at 8

Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
Example2

Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
Tags
'''
from typing import (
    List,
)
from lintcode import (
    Interval,
)
from typing import (
    List,
)
from lintcode import (
    Interval,
)
from heapq import *

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
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        ans = 0
        rooms = 0
        heap = []
        intervals.sort(key=lambda x:(x.start, x.end))
        print([(i.start, i.end) for i in intervals])
        for interval in intervals:
            while heap and interval.start >= heap[0]:
                heappop(heap)
                rooms -= 1
            heappush(heap, interval.end)
            rooms += 1
            ans = max(ans, rooms)
        return ans




from typing import (
    List,
)
from lintcode import (
    Interval,
)

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
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        ans = 0
        rooms = 0
        points = []
        for i in intervals:
            points.extend([(i.start, 1), (i.end, 0)])
        points.sort(key=lambda x:(x[0], x[1]))
        for p, type_ in points:
            if type_ == 1:
                rooms += 1
            else:
                rooms -= 1
            ans = max(ans, rooms)
        return ans