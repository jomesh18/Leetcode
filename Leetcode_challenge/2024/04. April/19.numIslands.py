'''
200. Number of Islands
Medium

22292

502

Add to List

Share
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        neighs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        def dfs(i, j):
            for di, dj in neighs:
                ni, nj = i+di, j+dj
                if 0<=ni<m and 0<=nj<n and grid[ni][nj] == '1':
                    grid[ni][nj] = '-1'
                    dfs(ni, nj)
            
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    grid[i][j] = '-1'
                    dfs(i, j)
        return ans