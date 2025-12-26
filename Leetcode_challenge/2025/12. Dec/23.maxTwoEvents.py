'''
2054. Two Best Non-Overlapping Events
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

 

Example 1:


Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
Example 2:

Example 1 Diagram
Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5
Explanation: Choose event 2 for a sum of 5.
Example 3:


Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8
Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
 

Constraints:

2 <= events.length <= 105
events[i].length == 3
1 <= startTimei <= endTimei <= 109
1 <= valuei <= 106
'''
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # top down dp
        # events.sort(key=lambda x:(x[0], x[1], -x[2]))
        
        # def helper(i):
        #     if i == n:
        #         return 0
        #     if memo[i] != -1: return memo[i]
        #     s, e, v = events[i]
        #     ans = v
        #     j = bisect_left(events, [e+1, 0, 0])
        #     if j != n:
        #         ans += max_from_right[j]
        #     ans = max(ans, helper(i+1))
        #     memo[i] = ans
        #     return ans

        # n = len(events)
        # memo = [-1]*n
        # max_from_right = [0]*n
        # max_from_right[-1] = events[-1][2]
        # for i in range(n-2, -1, -1):
        #     max_from_right[i] = max(max_from_right[i+1], events[i][2])
        # return helper(0)


        # bottom up dp
        n = len(events)
        events.sort(key=lambda x:(x[0], x[1], -x[2]))
        max_from_right = [0]*n
        max_from_right[-1] = events[-1][2]
        for i in range(n-2, -1, -1):
            max_from_right[i] = max(max_from_right[i+1], events[i][2])
        dp = [-1]*(n+1)
        dp[n] = 0
        for i in range(n-1, -1, -1):
            dp[i] = max(events[i][2], dp[i+1])
            j = bisect_left(events, [events[i][1]+1, 0, 0])
            if j != n:
                dp[i] = max(dp[i], events[i][2] + max_from_right[j])
        
        return dp[0]
