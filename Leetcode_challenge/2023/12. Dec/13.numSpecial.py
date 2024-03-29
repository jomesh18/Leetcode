'''
1582. Special Positions in a Binary Matrix
Easy

1028

38

Add to List

Share
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

Example 1:


Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
Example 2:


Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
'''
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        count = 0
        rows = [0]*m
        cols = [0]*n
        def ok(r, c):
            rc = 0
            cc = 0
            for i in range(m):
                if mat[i][c] == 1:
                    rc += 1
            for i in range(n):
                if mat[r][i] == 1:
                    cc += 1
            return (rc == 1 and cc == 1)
            
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if ok(i, j):
                        count += 1
        return count


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        count = 0
        rows = [0]*m
        cols = [0]*n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    count += 1
                    
        return count
                    