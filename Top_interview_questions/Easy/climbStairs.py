'''
Climbing Stairs

Solution
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
 

Constraints:

1 <= n <= 45
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        for i in range(2, n):
            dp[i%2] = dp[(i-1)%2] + dp[(i-2)%2]
        return dp[(n-1)%2]

class Solution:
    def climbStairs(self, n: int) -> int:
        dp, ans = [1, 1], 1
        for i in range(2, n+1):
            ans = dp[0] + dp[1]
            dp[0], dp[1] = dp[1], ans
        return ans


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        a, b = 1, 2
        for _ in range(2, n):
            b, a = a+b, b
        return b

# def climbStairs3(self, n):
#     if n == 1:
#         return 1
#     a, b = 1, 2
#     for i in xrange(2, n):
#         tmp = b
#         b = a+b
#         a = tmp
#     return b

n = 2
n = 3
# n = 4

sol = Solution()
print(sol.climbStairs(n))
