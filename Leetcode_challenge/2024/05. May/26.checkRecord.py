'''
552. Student Attendance Record II
Hard

2224

284

Add to List

Share
An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

 

Example 1:

Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
Example 2:

Input: n = 1
Output: 3
Example 3:

Input: n = 10101
Output: 183236316
 

Constraints:

1 <= n <= 105
'''
# memory limit exceeded
# class Solution:
#     def checkRecord(self, n: int) -> int:
#         MOD = 10 ** 9 + 7
#         memo = {}
#         def helper(i, absent, last_late):
#             if i == n:
#                 return 1
#             if (i, absent, last_late) in memo: return memo[(i, absent, last_late)]
#             ans = 0
#             if not absent:
#                 ans = (ans + helper(i+1, True, 0)) % MOD
#             if last_late < 2:
#                 ans = (ans + helper(i+1, absent, last_late+1)) % MOD
#             ans = (ans + helper(i+1, absent, 0)) % MOD
#             memo[(i, absent, last_late)] = ans
#             return ans
#         return helper(0, False, 0)

# accepted
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]
    
        for t in [True, False]:
            for last_late in range(3):
                dp[n][t][last_late] = 1
                
        for i in range(n-1, -1, -1):
            for absent in [True, False]:
                for last_late in range(3):
                    if not absent:
                        dp[i][absent][last_late] = (dp[i][absent][last_late] + dp[i+1][True][0]) % MOD
                    if last_late < 2:
                        dp[i][absent][last_late] = (dp[i][absent][last_late] + dp[i+1][absent][last_late+1]) % MOD
                    dp[i][absent][last_late] = (dp[i][absent][last_late] + dp[i+1][absent][0]) % MOD
        return dp[0][False][0]