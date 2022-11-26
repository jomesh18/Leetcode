'''
1235. Maximum Profit in Job Scheduling
Hard

4254

48

Add to List

Share
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:



Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 

Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 109
1 <= profit[i] <= 104
'''
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        jobs.sort(key=lambda x:(x[0], x[1], -x[2]))
        def find_next(curr):
            beg, end = curr+1, len(jobs)
            while beg < end:
                mid = (beg+end)//2
                if jobs[mid][0] >= jobs[curr][1]:
                    end = mid
                else:
                    beg = mid + 1
            return beg
        memo = {}
        def dfs(curr):
            if curr == len(jobs):
                return 0
            if curr in memo: return memo[curr]
            next_job = find_next(curr)
            incl_curr = jobs[curr][2] + (dfs(next_job) if next_job < len(jobs) else 0)
            excl_curr = dfs(curr+1)
            ans = max(incl_curr, excl_curr)
            memo[curr] = ans
            return ans
        return dfs(0)
        