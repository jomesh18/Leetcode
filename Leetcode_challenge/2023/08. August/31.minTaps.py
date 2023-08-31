'''
1326. Minimum Number of Taps to Open to Water a Garden
Hard

2381

140

Add to List

Share
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

 

Example 1:


Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]
Example 2:

Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.
 

Constraints:

1 <= n <= 104
ranges.length == n + 1
0 <= ranges[i] <= 100
'''
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = [[max(0, i-ranges[i]), i+ranges[i]] for i in range(n+1)]
        intervals.sort(key=lambda x:x[0])
        # print(intervals)
        count = 0
        prev_l, prev_r = 0, 0
        right = 0
        while right <= n:
            count += 1
            end = prev_r
            chosen = None
            while right <= n and intervals[right][0] <= prev_r:
                if right == 0 or end < intervals[right][1]:
                    end = intervals[right][1]
                    chosen = right
                right += 1
            # print(right, count, chosen, end)
            if end >= n: return count
            if (chosen is None and right <= n and intervals[right][0] > prev_r) or (right >= n and end < n):
                return -1

            prev_l, prev_r = intervals[chosen]
            # print(right, count, chosen, end)
        return count