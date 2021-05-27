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

#using stack, dfs

# class Graph:
#     def __init__(self, row, column, g):
#         self.row = row
#         self.column = column
#         self.g = g

#     def is_safe(self, i, j):
#         return i>=0 and i<self.row and j>=0 and j<self.column and self.g[i][j]=="1" and self.visited[i][j] is False

#     def count_islands(self):
#         self.visited = [[False for _ in range(self.column)] for _ in range(self.row)]
#         self.count = 0
#         for i in range(self.row):
#             for j in range(self.column):
#                 if self.is_safe(i, j):
#                     self.dfs(i,j)
#                     self.count += 1
#         return self.count

#     def dfs(self, i, j):
#         self.neighbors = [(-1, 0), (0, -1), (0, +1), (+1, 0)]
#         if self.is_safe(i, j):
#             self.visited[i][j] = True
#             for u, v in self.neighbors:
#                 self.dfs(i+u, j+v)

# class Solution:
#     def numIslands(self, grid: [[str]]) -> int:
#         g = Graph(len(grid), len(grid[0]), grid)
#         return g.count_islands()


# using bfs

# import pprint
# from collections import deque

# class Graph:

#     def __init__(self, row, column, g):
#         self.row = row
#         self.column = column
#         self.g = g

#     def is_safe(self, i, j):
#         return i>=0 and i<self.row and j>=0 and j<self.column and self.g[i][j]=='1' and not self.visited[i][j]

#     def bfs(self, i, j):
#         self.neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
#         q = deque([(i, j)])
#         while q:
#             l = len(q)
#             for _ in range(l):
#                 u, v = q.popleft()
#                 if self.is_safe(u, v):
#                     self.visited[u][v] = True
#                     pprint.pprint((self.visited))
#                     for x, y in self.neighbors:
#                         if self.is_safe(u+x, v+y):
#                             q.append((u+x, v+y))

#     def count_islands(self):
#         self.visited = [[False for _ in range(self.column)] for _ in range(self.row)]
#         self.count = 0
#         for i in range(self.row):
#             for j in range(self.column):
#                 if self.is_safe(i, j):
#                     self.bfs(i, j)
#                     self.count += 1
#         return self.count

# class Solution:
#     def numIslands(self, grid: [[str]]) -> int:
#         g = Graph(len(grid), len(grid[0]), grid)
#         return g.count_islands()

# from leetcode, dfs, modifies input, not using visited
def numIslands(self, grid):
    if not grid:
        return 0
        
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                self.dfs(grid, i, j)
                count += 1
    return count

def dfs(self, grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '#'
    self.dfs(grid, i+1, j)
    self.dfs(grid, i-1, j)
    self.dfs(grid, i, j+1)
    self.dfs(grid, i, j-1)

# from leetcode, by stefanpochmann

def numIslands(self, grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

# from leetcodde, bfs

from collections import deque
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid:
            return 0   
        count = 0
        check = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =='1' and check[i][j]== False:
                    count += 1
                    self.search(grid,check,i,j)
        return count       
    def search(self,grid,check,i,j):
        qu = deque([(i,j)])
        while qu:
            i, j = qu.popleft()
            if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=='1' and check[i][j]==False:
                check[i][j] = True
                qu.extend([(i-1,j),(i+1,j),(i,j-1),(i,j+1)])

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# Output: 1
s = Solution()
print(s.numIslands(grid))
