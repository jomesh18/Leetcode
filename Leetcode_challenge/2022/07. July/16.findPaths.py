'''
576. Out of Boundary Paths
Medium

2015

202

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
Accepted
79,021
Submissions
188,827
'''
#brute force, 4**n
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if startRow < 0 or startColumn < 0 or startRow == m or startColumn == n:
            return 1
        if maxMove == 0: return 0
        return (self.findPaths(m, n, maxMove-1, startRow-1, startColumn)+
                self.findPaths(m, n, maxMove-1, startRow, startColumn-1) +
                self.findPaths(m, n, maxMove-1, startRow, startColumn+1) + 
                self.findPaths(m, n, maxMove-1, startRow+1, startColumn))%(10**9+7)

#accepted, recursion with memo
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def helper(m, n, N, i, j):
            if i < 0 or j < 0 or i == m or j == n:
                return 1
            if N == 0: return 0
            return (helper(m, n, N-1, i-1, j) +
                    helper(m, n, N-1, i, j-1) +
                    helper(m, n, N-1, i, j+1) + 
                    helper(m, n, N-1, i+1, j))%(10**9+7)
        return helper(m, n, maxMove, startRow, startColumn)
