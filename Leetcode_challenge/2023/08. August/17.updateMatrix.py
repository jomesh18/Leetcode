'''
542. 01 Matrix
Medium

7997

358

Add to List

Share
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    mat[i][j] = -1
        
        neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        ans = [[0]*n for _ in range(m)]
        
        level = 0
        while q:
            nq = []
            for i, j in q:
                for di, dj in neighbors:
                    ni, nj = i+di, j+dj
                    if 0<=ni<m and 0<=nj<n and mat[ni][nj] == 1:
                        mat[ni][nj] = -1
                        nq.append((ni, nj))
                        ans[ni][nj] = level + 1
            q = nq[:]
            level += 1
        return ans
        