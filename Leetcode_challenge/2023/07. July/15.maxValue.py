'''
1751. Maximum Number of Events That Can Be Attended II
Hard

1070

18

Add to List

Share
You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.

 

Example 1:



Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7
Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
Example 2:



Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
Output: 10
Explanation: Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
Example 3:



Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
Output: 9
Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.
 

Constraints:

1 <= k <= events.length
1 <= k * events.length <= 106
1 <= startDayi <= endDayi <= 109
1 <= valuei <= 106
'''
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x:x[0])
        # def binary_search(arr, val, lo, hi):
        #     while lo < hi:
        #         mid = (lo+hi)//2
        #         if events[mid][0] <= val:
        #             lo = mid + 1
        #         else:
        #             hi = mid
        #     return lo
    
        n = len(events)
        memo = [[None]*n for _ in range(k+1)]
        def dfs(count, i):
            if i == n or count == 0:
                return 0
            if memo[count][i] is not None: return memo[count][i]
            ans = dfs(count, i+1)
            s, e, v = events[i]
            # j = binary_search(events, e, lo=i, hi=n)
            j = bisect_right(events, [e,float('inf'),float('inf')], lo=i, hi=n)
            temp = 0
            if j < n:
                temp = dfs(count-1, j)
            ans = max(ans, v + temp)
            memo[count][i] = ans
            return ans
        return dfs(k, 0)
