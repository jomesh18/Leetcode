'''
Spiral Matrix

Solution
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        tr, br, lc, rc = 0, m-1, 0, n-1
        ans = []
        while tr < br and lc < rc:
            for i in range(lc, rc):
                ans.append(matrix[tr][i])
            for i in range(tr, br):
                ans.append(matrix[i][rc])
            for i in range(rc, lc, -1):
                ans.append(matrix[br][i])
            for i in range(br, tr, -1):
                ans.append(matrix[i][lc])
            tr += 1
            br -= 1
            lc += 1
            rc -= 1
        if br < tr or rc < lc:
            return ans
        if tr != br:
            for i in range(tr, br+1):
                ans.append(matrix[i][lc])
        elif lc != rc:
            for i in range(lc, rc+1):
                ans.append(matrix[tr][i])
        else:
            ans.append(matrix[tr][lc])
        return ans