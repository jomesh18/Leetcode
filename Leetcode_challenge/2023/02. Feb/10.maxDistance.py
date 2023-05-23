'''
1162. As Far from Land as Possible
Medium

2972

74

Add to List

Share
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
'''
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = dp[i-1][j] + 1 
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
        # print(dp)       
        ans = -1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i < m-1:
                        dp[i][j] = min(dp[i][j], dp[i+1][j]+1)
                    if j < n-1:
                        dp[i][j] = min(dp[i][j], dp[i][j+1]+1)
                    ans = max(ans, dp[i][j])
        # print(dp)
        return ans if ans != float('inf') else -1