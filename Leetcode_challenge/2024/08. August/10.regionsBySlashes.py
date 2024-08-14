'''
959. Regions Cut By Slashes
Medium

3359

669

Add to List

Share
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

 

Example 1:


Input: grid = [" /","/ "]
Output: 2
Example 2:


Input: grid = [" /","  "]
Output: 1
Example 3:


Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 30
grid[i][j] is either '/', '\', or ' '.
'''
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        N = 3*n
        mat = [[0]*N for _ in range(N)]
        for r in range(n):
            for c in range(n):
                if grid[r][c] == '/':
                    mat[3*r][3*c+2] = 1              
                    mat[3*r+1][3*c+1] = 1
                    mat[3*r+2][3*c] = 1
                elif grid[r][c] == '\\':
                    mat[3*r][3*c] = 1
                    mat[3*r+1][3*c+1] = 1
                    mat[3*r+2][3*c+2] = 1
                    
        def flood_fill(i, j):
            mat[i][j] = 1
            for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N and mat[ni][nj] == 0:
                    flood_fill(ni, nj)
            
        ans = 0
        for i in range(N):
            for j in range(N):
                if mat[i][j] == 0:
                    ans += 1
                    flood_fill(i, j)
        return ans