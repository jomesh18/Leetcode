'''
861. Score After Flipping Matrix
Medium

1847

188

Add to List

Share
You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

 

Example 1:


Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
Example 2:

Input: grid = [[0]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] is either 0 or 1.
'''
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for r in range(m):
            if grid[r][0] == 0:
                for c in range(n):
                    grid[r][c] = 1 - grid[r][c]
        # print(grid)
        for c in range(n):
            count = 0
            for r in range(m):
                count += grid[r][c]
            if count < (m+1)//2:
                for i in range(m):
                    grid[i][c] = 1 - grid[i][c]
        # print(grid)
        for r in range(m):
            curr = 0
            for c in range(n):
                curr = (curr<<1)+grid[r][c]
            ans += curr
        return ans