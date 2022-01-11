'''
62. Unique Paths
Medium

7056

267

Add to List

Share
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.
'''

#naive dfs, tle
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         self.count = 0
#         def dfs(i, j):
#             if (i, j) == (m-1, n-1):
#                 self.count += 1
#             for u, v in ((i, j+1), (i+1, j)):
#                 if 0<=u<m and 0<=v<n:
#                     dfs(u, v)
#         dfs(0, 0)
#         return self.count


#dfs with visited, accepted
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = {}
        def dfs(i, j, count):
            if (i, j) == (m-1, n-1):
                count += 1
                return count
            temp_count = 0
            for u, v in ((i, j+1), (i+1, j)):
                if 0<=u<m and 0<=v<n:
                    if (u, v) not in visited:
                        visited[(u, v)] = dfs(u, v, count)
                    temp_count += visited[(u, v)]
            return count+temp_count
        ans = dfs(0, 0, 0)
        # print(visited)
        return ans

# recursive, tle
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def helper(i, j):
            if not (i<m and j<n): return 0
            if i == m-1 and j == n-1:
                return 1
            return helper(i+1, j) + helper(i, j+1)
        return helper(0, 0)

#recursive with memoization
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[None for _ in range(n)] for _ in range(m)]
        def helper(i, j):
            if not (i<m and j<n): return 0
            if memo[i][j] is not None: return memo[i][j]
            if i == m-1 and j == n-1:
                return 1
            memo[i][j] = helper(i+1, j) + helper(i, j+1)
            return memo[i][j]
        return helper(0, 0)

#iterative dp with tablulation dp[i][j] denote no of paths from (0, 0) to (i, j) (in memo dp[i][j] denoted paths from (i, j) to (m-1, n-1))
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

#space optimized dp O(2*n) space, 
class Solution:
    def uniquePaths(self, m, n):
        dp = [[1]*n for i in range(2)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i&1][j] = dp[(i-1)&1][j] + dp[i&1][j-1]
        return dp[(m-1)&1][-1]

# Or still better yet, in this case, you can use a single vector as well. 
# We are only accessing same column from previous row which can be given by dp[j] and previous column of current row which can be given by dp[j-1]. 
# So the above code can be further simplfied

class Solution:
    def uniquePaths(self, m, n):
        if m>n: m, n = n, m
        dp = [1]*n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]

m = 7
n = 3
# Output: 28

# m = 3
# n = 3
# Output: 6

# m = 100
# n = 100
# # Output: 22750883079422934966181954039568885395604168260154104734000

sol = Solution()
print(sol.uniquePaths(m, n))
