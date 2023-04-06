'''
1254. Number of Closed Islands
Medium

3328

105

Add to List

Share
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
'''
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            ans = True
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                ans = False
            for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ni, nj = i+di, j+dj
                if 0<=ni<m and 0<=nj<n and grid[ni][nj] == 0 and not visited[ni][nj]:
                    visited[ni][nj] = True
                    ans &= dfs(ni, nj)
            return ans
        
        count = 0
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visited[i][j]:
                    visited[i][j] = True
                    if dfs(i, j):
                        # print(i, j)
                        count += 1
        return count