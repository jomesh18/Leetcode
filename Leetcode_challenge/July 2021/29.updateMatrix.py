'''
01 Matrix

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
from collections import deque
class Solution:
    def updateMatrix(self, mat: [[int]]) -> [[int]]:
        row = len(mat)
        col = len(mat[0])
        res = [[0] * col for _ in range(row)]
        def bfs(i, j):
            q = deque([(i, j, 0)])
            neighbours = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            visited = set((i, j))
            while q:
                curr = q.popleft()
                u, v, lev = curr
                if (u, v) in visited:
                    continue
                visited.add((u, v))
                if mat[u][v] == 0:
                    return lev
                for a, b in neighbours:
                    if 0 <= u+a < row and 0 <= v+b < col:
                        q.append((u+a, v+b, lev+1))

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    res[i][j] = bfs(i, j)
        return res

# mat = [[0,0,0],[0,1,0],[0,0,0]]
# # Output: [[0,0,0],[0,1,0],[0,0,0]]

mat = [[0,0,0],[0,1,0],[1,1,1]]
# # Output: [[0,0,0],[0,1,0],[1,2,1]]

mat = [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,0,0]]
# Output: 

sol = Solution()
print(sol.updateMatrix(mat))
