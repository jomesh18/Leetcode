'''
1335. Minimum Difficulty of a Job Schedule
Hard

1103

127

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
61,063
Submissions
107,434
'''
#my try, top down memoization, accepted Runtime: 6929 ms, faster than 5.01% of Python3 online submissions for Minimum Difficulty of a Job Schedule.
# Memory Usage: 15.1 MB, less than 52.24% of Python3 online submissions for Minimum Difficulty of a Job Schedule.
# class Solution:
#     def minDifficulty(self, jobDifficulty: [int], d: int) -> int:
#         if len(jobDifficulty) < d:
#             return -1
#         dp = {}
#         def helper(i, days_left):
#             if (i, days_left) in dp: return dp[(i, days_left)]
#             if days_left == 1:
#                 return max(jobDifficulty[i:])
#             diff = float("inf")
#             for k in range(i, len(jobDifficulty)-days_left+1):
#                 diff = min(diff, max(jobDifficulty[i:k+1]) + helper(k+1, days_left-1))
#             dp[(i, days_left)] = diff
#             return diff
            
#         return helper(0, d)


#top down memo
# class Solution:
#     def minDifficulty(self, jobDifficulty: [int], d: int) -> int:
#         l = len(jobDifficulty)
#         if l < d:
#             return -1
#         hardest_job_remaining = [0]*l
#         hardest_job = 0
#         for i in range(l-1, -1, -1):
#             hardest_job = max(hardest_job, jobDifficulty[i])
#             hardest_job_remaining[i] = hardest_job
#         dp = {}
#         def helper(i, day):
#             if day == d:
#                 return hardest_job_remaining[i]
#             if (i, day) in dp: return dp[(i, day)]
#             best = float("inf")
#             hardest = 0
#             for k in range(i, l-(d-day)):
#                 hardest = max(hardest, jobDifficulty[k])
#                 best = min(best, hardest + helper(k+1, day+1))
#             dp[(i, day)] = best
#             return best
#         return helper(0, 1)

#bottom up dp
class Solution:
    def minDifficulty(self, jobDifficulty: [int], d: int) -> int:
        l = len(jobDifficulty)
        if l < d:
            return -1
        dp = [[float("inf")]*(d+1) for _ in range(l)]
        dp[-1][d] = jobDifficulty[-1]
        for i in range(l-2, -1, -1):
            dp[i][d] = max(dp[i+1][d], jobDifficulty[i])

        for day in range(d-1, 0, -1):
            for i in range(day-1, l-(d-day)):
                hardest = 0
                for k in range(i, l-(d-day)):
                    hardest = max(hardest, jobDifficulty[k])
                    dp[i][day] = min(dp[i][day], hardest + dp[k+1][day+1])
        return dp[0][1]


jobDifficulty = [6,5,4,3,2,1]
d = 2
#Output: 7

jobDifficulty = [6,5,4,3,2,1,7]
d = 2

# jobDifficulty = [9,9,9]
# d = 4
# # Output: -1

# jobDifficulty = [1,1,1]
# d = 3
# Output: 3

jobDifficulty = [11,111,22,222,33,333,44,444]
d = 6
# Output: 843

sol = Solution()
print(sol.minDifficulty(jobDifficulty, d))
