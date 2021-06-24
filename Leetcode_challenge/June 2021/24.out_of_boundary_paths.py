'''
Out of Boundary Paths

There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent four cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

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
    0 <= startRow <= m
    0 <= startColumn <= n

'''
from collections import deque
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def bfs(c, d):
            neighbours = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            count = 0
            level = 0
            q = deque([(c, d)])
            while level < maxMove:
                l = len(q)
                for _ in range(l):
                    i, j = q.popleft()
                    for a, b in neighbours:
                        if not 0<=i+a<m or not 0<=j+b<n:
                            count += 1
                        if 0<=i+a<m and 0<=j+b<n:
                            q.append((i+a, j+b))
                level += 1
            return count%(10**9+7)
        return bfs(startRow, startColumn)

m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0
# Output: 6

# m = 1
# n = 3
# maxMove = 3
# startRow = 0
# startColumn = 1
# # Output: 12

m = 2
n = 3
maxMove = 8
startRow = 1
startColumn = 0
# Output: 1104

m = 7
n = 6
maxMove = 13
startRow = 0
startColumn = 2
# Output: 1659429

s = Solution()
print(s.findPaths(m, n, maxMove, startRow, startColumn))
