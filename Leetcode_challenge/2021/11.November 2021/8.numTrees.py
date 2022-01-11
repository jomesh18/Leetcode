'''
96. Unique Binary Search Trees
Medium

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:

Input: n = 3
Output: 5

Example 2:

Input: n = 1
Output: 1

 

Constraints:

    1 <= n <= 19

Accepted
420,028
Submissions
739,793
'''

#recurive, O(3*n)
# class Solution:
#     def numTrees(self, n: int) -> int:
#         if n<=1: return 1
#         ans = 0
#         for i in range(1, n+1):
#             ans += self.numTrees(i-1)*self.numTrees(n-i)
#         return ans
            
# (Dynamic Programming - Memoization) O(n**2)
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1] + [None]*(n-1)
        def helper(n):
            if n<=1: return 1
            if dp[n] is not None: return dp[n]
            ans = 0
            for i in range(1, n+1):
                dp[i-1] = helper(i-1)
                dp[n-i] = helper(n-i)
                ans += dp[i-1]*dp[n-i]
            return ans
        return helper(n)

# (Dynamic Programming - Tabulation) O(n*2)
# class Solution:
#     def numTrees(self, n: int) -> int:
#         dp = [1, 1] + [0]*(n-1)
#         for i in range(2, n+1):
#             for j in range(1, i+1):
#                 dp[i] += dp[j-1] * dp[i-j]
#         return dp[n]

n = 3
# Output: 5

# n = 1
# Output: 1

n = 19
# Output: 1767263190

sol = Solution()
print(sol.numTrees(n))
