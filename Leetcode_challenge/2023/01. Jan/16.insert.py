'''
57. Insert Interval
Medium

7001

486

Add to List

Share
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def binary_search(lo, hi, target, pos, arr):
            while lo < hi:
                mid = (lo+hi)//2
                if target > arr[mid][pos]:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        if not intervals: return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval]+ intervals
        if intervals[-1][1] < newInterval[0]:
            return intervals +[newInterval]
        
        start = binary_search(0, len(intervals), newInterval[0], 0, intervals)
        end = binary_search(0, len(intervals), newInterval[1], 0, intervals)
        # print(start, end)
        if (start == len(intervals) and intervals[start-1][1] >= newInterval[0]) or (start > 0 and start < len(intervals) and intervals[start-1][1] >= newInterval[0]):
            start -= 1
        if (end == len(intervals) and intervals[end-1][1] >= newInterval[1]) or (end > 0 and end < len(intervals) and intervals[end][0] > newInterval[1]):
            end -= 1
        if start > end:
            end = start
        # print(start, end)
        if start > 0 and start < len(intervals) and end < len(intervals) and intervals[start-1][1] < newInterval[0] and intervals[end][0] > newInterval[1]:
            return intervals[:start]+[newInterval]+intervals[end:]
        return intervals[:start]+[[min(intervals[start][0], newInterval[0]) if start < len(intervals) else newInterval[0], max(intervals[end][1], newInterval[1]) if end < len(intervals) else newInterval[1]]]+intervals[end+1:]


# O(n) linear search
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        ns, ne = newInterval
        for i, (s, e) in enumerate(intervals):
            if s > ne:
                return ans + [[ns, ne]] + intervals[i:]
            elif min(ne, e) - max(ns, s) >= 0:
                ns = min(ns, s)
                ne = max(ne, e)
            else:
                ans.append([s, e])
        return ans + [[ns,ne]]


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        left = [i for i in intervals if i[1] < s]
        right = [i for i in intervals if i[0] > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[-len(right)-1][1])
        return left + [[s, e]] + right