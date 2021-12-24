'''
56. Merge Intervals
Medium

10979

459

Add to List

Share
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
Accepted
1,188,726
Submissions
2,720,323
'''
#using sorting
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         if len(intervals)<= 1: return intervals
#         intervals.sort()
#         print(intervals)
#         res = []
#         i,  j = 0, 1
#         start, end = intervals[0]
#         while j < len(intervals):
#             if intervals[i][1] >= intervals[j][0]:
#                 start = min(start, intervals[i][0])
#                 end = max(intervals[i][1], intervals[j][1])
#                 if intervals[i][1] < intervals[j][1]:
#                     i = j
#                 j += 1
#             else:
#                 res.append([start, end])
#                 start, end = intervals[j]
#                 i = j
#                 j += 1
#         res.append([start, end])
#         return res


#using sorting, from leetcode
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:

#         intervals.sort(key=lambda x: x[0])

#         merged = []
#         for interval in intervals:
#             # if the list of merged intervals is empty or if the current
#             # interval does not overlap with the previous, simply append it.
#             if not merged or merged[-1][1] < interval[0]:
#                 merged.append(interval)
#             else:
#             # otherwise, there is overlap, so we merge the current and previous
#             # intervals.
#                 merged[-1][1] = max(merged[-1][1], interval[1])

#         return merged