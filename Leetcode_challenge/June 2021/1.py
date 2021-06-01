'''
Max Area of Island
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
'''
import pprint
class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        r, c = len(grid), len(grid[0])
        count = 0
        visited = set()
        def dfs(i, j, count):
            if (i, j) not in visited:
                visited.add((i,j))
                count += 1
                for rr, cc in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                    new_r, new_c = i+rr, j+cc
                    if 0<=new_r<r and 0<=new_c<c and grid[new_r][new_c] != 0 and (new_r, new_c) not in visited:
                        count = dfs(new_r, new_c, count)
            return count

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (i, j) not in visited:
                    # print(i, j)
                    count = max(count, dfs(i, j, 0))
                    # print(count, visited)
        return count

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# print(len(grid), len(grid[0]))
# pprint.pprint(grid)

grid = [[0,0,0,0,0,0,0,0]]
# Output: 0

s = Solution()
print(s.maxAreaOfIsland(grid))
