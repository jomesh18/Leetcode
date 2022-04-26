'''
Number of Islands

Solution
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
        neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        def dfs(i, j):
            grid[i][j] = '#'
            for u, v in neighbors:
                if 0<=u+i<m and 0<=v+j<n and grid[u+i][v+j] == '1':
                    dfs(u+i, v+j)
                    
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res        
        