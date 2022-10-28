'''
Longest Increasing Path in a Matrix

Solution
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
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        dp = [[-1]*n for _ in range(m)]
        def dfs(i, j):
            ans = 0
            for u, v in neighbors:
                ni, nj = i+u, j+v
                if 0<=ni<m and 0<=nj<n and matrix[ni][nj] > matrix[i][j]:
                    if dp[ni][nj] != -1:
                        ans = max(ans, dp[ni][nj])
                    else:
                        ans = max(ans, dfs(ni, nj))
            dp[i][j] = 1 + ans
            return dp[i][j]
        res = 0
        for i in range(m):
            for j in range(n):
                if dp[i][j] == -1:
                    dp[i][j] = dfs(i, j)
                    res = max(res, dp[i][j])
        return res


# topological sort (kahn's algorithm)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        indegree = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                for u, v in neighbors:
                    ni, nj = i+u, j+v
                    if 0<=ni<m and 0<=nj<n and matrix[ni][nj] < matrix[i][j]:
                        indegree[i][j] += 1
        q = []
        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    q.append((i, j))
                    
        longest = 0
        while q:
            new_q = []
            for i, j in q:
                for u, v in neighbors:
                    ni, nj = i+u, j+v
                    if 0<=ni<m and 0<=nj<n and matrix[ni][nj] > matrix[i][j]:
                        indegree[ni][nj] -= 1
                        if indegree[ni][nj] == 0:
                            new_q.append((ni, nj))
            longest += 1
            q = new_q[:]
        return longest