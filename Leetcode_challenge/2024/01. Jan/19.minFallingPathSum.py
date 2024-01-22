'''
931. Minimum Falling Path Sum
Medium

6076

154

Add to List

Share
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

Example 1:


Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:


Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100
'''
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        curr = matrix[0]
        prev = [0]*n
        for i in range(1, m):
            prev = curr[:]
            for j in range(n):
                curr[j] = matrix[i][j] + min(prev[j], prev[j-1] if j > 0 else float('inf'), prev[j+1] if j < n-1 else float('inf'))
            # print(curr)
        return min(curr)