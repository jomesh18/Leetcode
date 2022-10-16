'''
1335. Minimum Difficulty of a Job Schedule
Hard

1674

179

Add to List

Share
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

 

Example 1:


Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.
 

Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10
Accepted
86,646
Submissions
153,247
'''
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        max_from_right = [0]*(n-1)+[jobDifficulty[-1]]
        for i in range(n-2, -1, -1):
            max_from_right[i] = max(jobDifficulty[i], max_from_right[i+1])
        memo = {}
        if d > n: return -1
        def helper(i, rem, curr_diff):
            if (i, rem, curr_diff) in memo: return memo[(i, rem, curr_diff)]
            if rem == 0: return curr_diff if i >= n else max(max_from_right[i], curr_diff)
            # if i == n and rem > 0: return float('inf')
            # if i == n and rem < 0: return float('inf')
            # if i == n and rem == 0: return curr_diff
            if i == n: return float('inf')
            addtolast = helper(i+1, rem, max(curr_diff, jobDifficulty[i]))
            startnew = curr_diff + helper(i+1, rem-1, jobDifficulty[i])
            ans = min(addtolast, startnew)
            memo[(i, rem, curr_diff)] = ans
            return ans
        return helper(0, d, 0)