'''
576. Out of Boundary Paths
Medium

3337

252

Add to List

Share
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
Example 2:


Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
 

Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
'''
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        MOD = 10**9+7
        def dfs(i, j, rem):
            if i < 0 or i == m or j < 0 or j == n:
                return 1
            if rem == 0:
                return 0
            if (i, j, rem) in memo: return memo[(i, j, rem)]
            ans = 0
            for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ans = (ans + dfs(i+di, j+dj, rem-1)) % MOD
            memo[(i, j, rem)] = ans
            return ans
            
        return dfs(startRow, startColumn, maxMove)