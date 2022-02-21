'''
1288. Remove Covered Intervals
Medium

1757

42

Add to List

Share
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1
 

Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= li <= ri <= 105
All the given intervals are unique.
Accepted
89,553
Submissions
155,281
'''
# sort
class Solution:
    def removeCoveredIntervals(self, intervals: [[int]]) -> int:
        intervals.sort()
        count = 0
        right, left = -1, -1
        for l, r in intervals:
            if l > left and r > right:
                count += 1
                left = l
            right = max(r, right)
        return count

# sort left ascending, right descending
class Solution
    def removeCoveredIntervals(self, A):
        res = right = 0
        A.sort(key=lambda a: (a[0], -a[1]))
        for i, j in A:
            res += j > right
            right = max(right, j)
        return res

intervals = [[1,4],[3,6],[2,8]]
# Output: 2

# intervals = [[1,4],[2,3]]
# Output: 1

sol = Solution()
print(sol.removeCoveredIntervals(intervals))
