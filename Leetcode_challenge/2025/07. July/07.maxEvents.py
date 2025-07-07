'''
1353. Maximum Number of Events That Can Be Attended
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.

 

Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
 

Constraints:

1 <= events.length <= 105
events[i].length == 2
1 <= startDayi <= endDayi <= 105
'''
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        max_day = max(events[i][1] for i in range(len(events)))
        count = 0
        j = 0
        pq = []
        for curr_day in range(events[0][0], max_day+1):
            while j < len(events) and events[j][0] <= curr_day:
                heappush(pq, events[j][1])
                j += 1
            while pq and pq[0] < curr_day:
                heappop(pq)
            if pq:
                heappop(pq)
                count += 1

        return count
