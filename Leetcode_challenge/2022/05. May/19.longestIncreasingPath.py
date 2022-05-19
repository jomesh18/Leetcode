'''
329. Longest Increasing Path in a Matrix
Hard

5711

96

Add to List

Share
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
Accepted
339,756
Submissions
673,506
'''
#dfs with memoization
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        self.res = 1
        self.memo = [[0]*n for _ in range(m)]
        def dfs(i, j, curr):
            if self.memo[i][j]: return self.memo[i][j]
            ans = 1
            for u, v in ((i-1, j), (i, j-1), (i, j+1), (i+1, j)):
                if 0<=u<m and 0<=v<n and matrix[u][v] > matrix[i][j]:
                    ans = max(ans, curr + dfs(u, v, 1))
            self.memo[i][j] = ans
            if ans > self.res: self.res = ans
            return ans
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, 1)
        print(self.memo)
                
        return self.res

#using Kahn's algorithm for topological sorting
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        indegree = [[0]*n for _ in range(m)]
        
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        for i in range(m):
            for j in range(n):
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if 0<=ni<m and 0<=nj<n and matrix[i][j] < matrix[ni][nj]:
                        indegree[i][j] += 1
        q = []                        
        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    q.append((i, j))
        pathlen = 0
        while q:
            t = []
            for i, j in q:
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if 0<=ni<m and 0<=nj<n and matrix[ni][nj] < matrix[i][j]:
                        indegree[ni][nj] -= 1
                        if indegree[ni][nj] == 0: t.append((ni, nj))
            q = t[:]
            pathlen += 1
            
        return pathlen


def longestIncreasingPath(self, matrix):
    def dfs(i, j):
        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
        return dp[i][j]

    if not matrix or not matrix[0]: return 0
    M, N = len(matrix), len(matrix[0])
    dp = [[0] * N for i in range(M)]
    return max(dfs(x, y) for x in range(M) for y in range(N))