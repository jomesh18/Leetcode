'''
Making A Large Island
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
'''
#tle
# from collections import deque
# class Solution:
#     def largestIsland(self, grid: [[int]]) -> int:
#         res = 0
#         row, col = len(grid), len(grid[0])
#         def bfs(i, j):
#             count = 0
#             visited = set()
#             neighbors = ((-1, 0), (0, -1), (0, 1), (1, 0))
#             q = deque([(i,j)])
#             while q:
#                 u, v = q.popleft()
#                 if (u, v) not in visited:
#                     count += 1
#                     visited.add((u, v))
#                     for a, b in neighbors:
#                         if 0<=u+a<row and 0<=v+b<col and grid[u+a][v+b] == 1:
#                             q.append((u+a, v+b))
#             return count

#         for i in range(row):
#             for j in range(col):
#                 if grid[i][j] == 0:
#                     res = max(res, bfs(i, j))

#         return res if res else row*col

#from leetcode
class Solution:
    def largestIsland(self, grid: [[int]]) -> int:
        N = len(grid)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc

        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans

        area = {}
        index = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        ans = max(area.values() or [0])
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                    ans = max(ans, 1 + sum(area[i] for i in seen))
        return ans

grid = [[1,0],[0,1]]
# Output: 3

grid = [[1,1],[1,0]]
# # Output: 4

# grid = [[1,1],[1,1]]
# # Output: 4

grid = [[1,0,0,0,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1],[0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0],[1,0,1,1,0,0,0,0,1,0,0,1,1,1,0,0,1,1,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,1,1,1,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,1,0,1,1,1,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1],[1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,1,1,1,0,0,0,1,1,1,1,0,1,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1],[1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,1,1,0,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,1,0,1,0,1,1,1,0,0,1,0,0,1,1,0,0,0,1,0],[1,0,0,0,1,0,0,1,1,1,0,1,0,1,0,0,1,0,1,1,1,1,1,1,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,1,1,0,1,1,1,0,0,0,1,0,0,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1],[0,1,1,1,1,0,0,1,0,1,1,1,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,0,1,0,0,0,1,0,1,1,0,1,1,1,1,0,1,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0],[1,0,1,1,1,0,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,1,1,1,0,1,0,1,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0,1,1,0,1,0,0,0,0,1,0,0,1,1,1,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,1,1],[1,1,1,0,0,1,0,0,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,0,0,0,1,1,1,1,0,0,1,0,0,0,1,0,1,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,1,0,0,1,1,1,0,1,0,0,1,0,0,1,1,1,0,1,0,0,0,1,1,0,0,1,1,0,1,1,1],[1,1,1,0,0,1,0,1,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,0,1,0,1,1,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,1,0,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1],[0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,1,1,0,0,1,1,0,1,1,0,1,0,1,0,0,1,0,0,0,1,1,0,1,1],[0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,1,0,0,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,1,0,0,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0],[1,0,0,0,1,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,1,1,0,0,1,0,0,0,1,1,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,1,0,1,0,1,1,0,1,0,0,1,1,0,1,0,0,0],[1,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,0,1,0,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,1,1,0,1,1,1,0,1,0,0,1],[1,0,1,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,0,0,0,1,1,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1],[0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,1,0,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,1,1,1,1],[0,0,0,1,0,1,0,1,0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,0,1,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,0,0,0,0],[0,1,1,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,1,0,1,0,0,0,0,1,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1,1],[1,1,0,1,0,1,1,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,0,0,0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,0,1,0,1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0],[0,1,1,1,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,1,0,1,1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,0,1,0,0,0,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,0],[0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,0,1,0,0,1,1,1,0,1,1,0,1,1,1,0,1,1,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1,0,1],[0,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,0,0,0,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,1,1,1,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,0,0,1,1,1,1,0,1,0],[1,1,0,1,0,0,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,0,1,0,1,1,1,0,0,0,1,0,1,0,0,1,0,1,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,0,1,0,1],[0,0,1,0,1,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,1,0,0,0,1,0,1,1,0,1,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1],[1,0,0,0,1,0,0,1,1,1,1,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,1,1,0,1,1,1,1],[1,0,0,0,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,0,0,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0,0,1,0,0,1,1,1,0,0,1,1,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,0,1,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1],[1,0,1,0,0,0,1,1,1,0,0,1,0,0,0,1,1,0,0,0,0,0,1,1,0,1,0,1,1,0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,1,0],[1,1,1,1,1,1,0,1,1,0,1,0,0,0,1,1,0,1,0,1,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,1,0,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,0],[0,1,0,1,1,1,1,1,1,1,0,0,1,1,0,0,0,1,0,0,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,0,1,1,1,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,1,1],[0,1,1,1,0,0,0,0,0,1,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,1,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,0,1],[0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,0,1,1,1,0,0,1,1,1,1,1,0,0,0,1,0,0,1,1,1,0,0,0,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,0,1],[1,0,1,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1,1,0,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0],[1,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,1,0,1,0,1,1,0,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,0,1,0,0,1,0,0,1,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1,0],[1,0,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,1,1,1,1,0,0,0,1,0,0,1,0],[1,1,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,0,1,1,0,1,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,0,1,1,0,1,0,0,1,1,1,1],[0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,1,0,0],[0,1,0,0,0,0,1,1,0,0,1,0,0,1,1,0,1,1,0,1,0,0,1,0,1,0,0,0,0,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,1,1,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,1,0,0,1,0,1,0,0,0,1,1,1,1,1,1,0,1,0,0,1,0,0,0,1,0,1,1,0,0],[0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,1,1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,1,0,0,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,0,1,0,1,0,0,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,1,0,0,0,1,1,0,1,0,0,1,1,1,1,0,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,0,1,1,1,0,1,0,1],[0,0,1,1,1,0,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,1,1,1,0,0,0,0,1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,1,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,0,0,1,0,1,1,1,0,0,0,1,1],[1,1,0,1,0,1,0,1,1,1,1,0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,1,1,1,1],[0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1],[1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1,0,0,1,1,0,1,1,1,1,0,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,0,0],[0,1,1,0,1,1,0,1,1,1,0,0,1,1,0,0,1,0,0,0,0,1,0,1,1,0,0,0,1,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,0,0,1,0,1,0,0,0,0,1,0,0,1,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1],[0,1,1,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,0,0,1,0,0,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,1,0],[0,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0,0,1,0,0,0,0,1,1,0,1,0,1,0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,1,1,0],[0,0,1,1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,0],[0,0,1,0,0,0,1,1,1,0,0,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,1,0,1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,1,1,0,1,1,1,1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,1,1,1,1,0,1,1,0,0,0,1],[1,0,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,0,0,0,1,0,1,1,0,0,0,1,1,0,1,1,1,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,0,1],[0,0,0,1,1,0,0,0,0,1,0,0,1,0,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,0,0,1,1,0,1,0,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,0,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,0],[1,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,1,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,0,1,0,1,1,1,1],[1,0,0,1,0,1,1,0,0,1,0,1,0,1,1,0,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,1,0,1,1,0,1,0],[1,0,0,0,1,0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,1,1,0,1,1,0,0,0,1,0,1,1,0,1,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,1,1,1,0,1,1,0,0,1,0,0,0,0,0],[0,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,1,0,1,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,1,0,1,0,1,1,0,0,1,0,0,1,0,0,1,1,0,1,1,0,1,0,1,1,1,0,1],[0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,0,1,1,0,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,0,1],[0,1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,0,0,0,1,1,1,1,1,0,1,1,0,1,1,1],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,1,1,0,1,0,0,1,0,0,1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,0,0,1,0,0,1,1,1,1,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,0,0,1,0,1,1,1,1,1],[0,1,1,1,1,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,1,0,0],[1,0,0,1,1,1,0,0,1,0,1,0,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,1,0,0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,1],[1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,0,1,0,1,1],[1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,1,1,1,1,1,1,1,0,1,1,0,1,0,1,1,1,1,0,1,1,0,1,1,0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,0,1],[0,0,0,1,0,0,0,1,1,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,0,0,1,0,0,1,0,1,1,1,1,0,1,0,0,1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0,0,1,0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[0,0,1,0,1,1,0,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,1,0,1,0,1,1,1,0,1,1,0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,1,0,0,0,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0],[1,1,0,0,1,0,1,1,1,0,1,1,1,1,0,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0,1,0,1,0,1,1,1,1,0,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,1,0,0,1,0,0,1,1,0,1,1,1,1,0],[1,1,0,0,1,0,1,0,1,1,1,0,0,1,0,0,1,1,1,0,0,1,0,1,1,0,1,1,0,0,1,0,1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,0,0,0,0,1],[0,0,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,0,1,1,1,1,1,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,1,0,0,1,1,0,0,1,1,0,0,0,1,0,0,0],[1,1,0,1,0,1,0,1,1,1,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,0,0,0],[0,1,0,0,1,1,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,1],[0,1,1,0,0,1,1,0,1,0,1,1,0,0,1,1,1,0,1,0,1,1,0,0,1,0,1,1,1,0,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,0,1,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,0,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,0,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,1,1,0,0,1,0,1,1,0,0],[1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,0,1,1,1,0,1,1,0,0,1,0,1,0,1,0,0,1,1,1,0,1,0,0,1,0,0,1,1,0,1,0,0,1,0,1],[1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,1,0,1,0,1,1,0,0,0,0],[0,0,0,1,1,0,0,0,1,1,0,1,1,1,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,1],[0,1,0,1,0,0,1,0,1,1,0,0,1,1,0,0,1,0,1,0,1,1,0,0,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,1,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1,1,0,1,1,0,1,0,0,0,0,1,1,1,1,0,0],[0,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,1,1,1,0,0,0,1,0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,1,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1],[1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,0,1,0,1,0,0,1,1,0,1,0,0,1,1,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,1,1,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,1,0,1,1,0,0],[0,1,1,1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,0,1,0,0,1,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,1,0,0,0,0,0,1,0,1,1,0,0,0,1,1,0,1,0,0,0,0,1,0,0,1,0,1],[1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,0,1,0,1,1],[0,0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,0,0,1,1,0,1,1,0,1,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1,1,0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,0,0],[0,1,0,1,0,0,1,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,1,1,1,0,1,0,0,0,0,1,0,1,0,1,0,0,1,1,0,0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,1,1,0,1,1,0,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0,1,1,1,0,0],[0,1,1,1,0,1,0,0,0,0,1,1,0,1,0,1,1,0,1,1,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,1,0,1,1,0,0,1,0,1,0,0,1,0,1,1,0,0,1,0,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,0,1,0,0,1,1,0,1,0,1,0,0,1,0,1,1,0,1,0,1,0,0],[0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,1,1,1,0,0,1,1],[0,1,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,0,1,0,0,1,1,0,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,1,0,0,0,0,0,1,0,1,0],[1,0,1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1],[0,1,1,0,0,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,1,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1],[1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1,1,0,0,0,1,0,0,1,0,1,1,0,0,1,1,0,0,1,1,1,1,1,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0],[1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,1,0,0,1,1,0,1,1,1,1,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,1,0,1,0],[0,0,0,1,1,0,0,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,0,0,0,0,1,0,1,0,0,1,1,0,1,1,1,0,1,0,1,0,0,1,1,0,1,0,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1],[0,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,1,1,1,0,1,0,0,0,1,1,1,0,0,0,1,1,0,0,0,1,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,1,1,1,1,0,1,0,1,1,0,0,1,1,1,1,1,1,0,1,0,0,0,0,0,0],[1,1,1,1,1,1,1,0,0,1,1,0,1,0,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,1,1,0,0,1,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,1,0,1,1,0,1,1,1,0,0,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,1,1,0],[0,0,0,0,0,1,0,1,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1,0,0,0,1,0,1,0,0,1,0,0,0,1,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,0,0,0,1,0,0,1],[1,1,1,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1],[1,1,1,0,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0,1,1,1,1,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,1,1,0,0,1,0],[0,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,0,0,1,1,1,1,0,1,0,1,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,0,1,1,0,1],[1,1,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,0,1,1,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,0,1,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,0,1,0,0,1],[0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,1,0,1,1,0,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,1,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,0,0,0],[1,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,0],[1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0,0,1,1,0,1,1,1,0,0,1,0,1,1,0,1,1,1,1],[1,0,0,1,1,0,0,1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,1,0,1,0,0,1,0,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,1,1,0,0,1,0,0,0,0],[0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1,1,0,0,0,1,0,1,1,1,0,0,1,0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,1,0,0,1,0,1,1],[1,0,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,1,0,0,0,0,0,0,1,1,0,0,1,0,1,1,0,0,0,0,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,1,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,1,0,0,0,1,1,0,1,1,1,0,1,1,0,0,1,0,1,0,1,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,1,1,1,0,0,0,1,1,1,1,0,1,1,0,0,1,0,0,0,0,0,1,0,1,1,0,0,1,1,0,0,1,1,1,0,1,0,0,1,1,1,1,1,1,0,0,1,0,1,1,0,0,1,0,0,0,1,1,1,0,0,1,1,0,1,1,0,1,1,0,0],[0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,0,1,0,0,1,0,0],[0,0,0,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,1,1,0,0,0,0,1,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,1],[0,1,0,0,1,1,0,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,1,0,1,1,0,1,1,1,0,1,1,1,1,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,1,1,0,0,1,0,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,0],[1,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,1,0,1,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0],[1,1,1,0,1,0,0,1,0,1,0,0,1,1,1,0,1,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,0,0,1,0,1,1],[0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,1,1,0,1,1,0,1,1,0,0,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,1,1,1,0,1,0]]
print(len(grid), len(grid[0]))
# Output: 369

sol = Solution()
print(sol.largestIsland(grid))