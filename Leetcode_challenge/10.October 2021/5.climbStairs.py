'''
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
#dp
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [1, 1] + [None] * (n-1)
#         for i in range(2, n+1):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[n]

#dp constant space
class Solution:
    def climbStairs(self, n: int) -> int:
        dp, ans = [1, 1], 1
        for i in range(2, n+1):
            ans = dp[0] + dp[1]
            dp[0], dp[1] = dp[1], ans
        return ans
n = 2
# Output: 2

n = 3
# Output: 3

n = 4
# Output: 5

n = 5
#Output: 8

sol = Solution()
print(sol.climbStairs(n))
