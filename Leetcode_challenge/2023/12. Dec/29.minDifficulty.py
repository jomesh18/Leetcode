'''
1335. Minimum Difficulty of a Job Schedule
Hard

3332

315

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
'''
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n: return -1
        max_from_right = [0]*(n-1)+[jobDifficulty[-1]]
        for i in range(n-2, -1, -1):
            max_from_right[i] = max(max_from_right[i+1], jobDifficulty[i])
        memo = {}
        def helper(i, rem, curr_max_i):
            if i == n:
                return 0 if rem == 0 else float('inf')
            if rem == 1:
                return max_from_right[i]
            if (i, rem, curr_max_i) in memo: return memo[(i, rem, curr_max_i)]
            starting_new = jobDifficulty[curr_max_i] + helper(i+1, rem-1, i+1)
            adding_to_last = float('inf')
            if i+1 < n:
                adding_to_last = helper(i+1, rem, i+1 if jobDifficulty[i+1] > jobDifficulty[curr_max_i] else curr_max_i)
            ans = min(starting_new, adding_to_last)
            memo[(i, rem, curr_max_i)] = ans
            return ans
        return helper(0, d, 0)
