'''
85. Maximal Rectangle
Solved
Hard
Topics
premium lock icon
Companies
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= rows, cols <= 200
matrix[i][j] is '0' or '1'.
'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = (dp[i][j+1] + 1) if matrix[i][j] == '1' else 0

        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    col_len = n
                    for row in range(i, m):
                        col_len = min(col_len, dp[row][j])
                        if col_len == 0: break
                        ans = max(ans, (row-i+1)*col_len)
        return ans
