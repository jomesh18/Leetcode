'''
498. Diagonal Traverse
Solved
Medium
Topics
premium lock icon
Companies
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
'''
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        r, c = 0, 0
        ans = []
        up = True
        # print(m, n)
        for _ in range(m+n-1):
            if up:
                while r >= 0 and c < n:
                    ans.append(mat[r][c])
                    # print(up, r, c)
                    r -= 1
                    c += 1
                r += 1
                c -= 1
                if c < n-1:
                    c += 1
                else:
                    r += 1

            else:
                while r < m and c >= 0:
                    ans.append(mat[r][c])
                    r += 1
                    c -= 1
                    # print(up, r, c)
                r -= 1
                c += 1
                if r < m-1:
                    r += 1
                else:
                    c += 1
            up = not up

        return ans