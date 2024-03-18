'''
57. Insert Interval
Medium

10074

773

Add to List

Share
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

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
        ns, ne = newInterval
        if not intervals: return [newInterval]
        intervals.sort()
        if ne < intervals[0][0]: return [newInterval] + intervals
        if ns > intervals[-1][1]: return intervals + [newInterval]
        ans = []
        i = 0
        while i < len(intervals):
            s, e = intervals[i]
            if i != 0 and intervals[i-1][1] < ns and s > ne:
                ans.append(newInterval)
            if e < ns or s > ne:
                ans.append([s, e])
                i += 1
            else:
                curr_s = min(s, ns)
                curr_e = max(e, ne)
                while i < len(intervals) and intervals[i][0] <= curr_e:
                    curr_e = max(curr_e, intervals[i][1])
                    i += 1
                ans.append([curr_s, curr_e])
        return ans