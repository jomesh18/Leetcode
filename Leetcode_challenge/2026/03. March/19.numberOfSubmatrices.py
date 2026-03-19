'''
3212. Count Submatrices With Equal Frequency of X and Y
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.
 

Example 1:

Input: grid = [["X","Y","."],["Y",".","."]]

Output: 3

Explanation:



Example 2:

Input: grid = [["X","X"],["X","Y"]]

Output: 0

Explanation:

No submatrix has an equal frequency of 'X' and 'Y'.

Example 3:

Input: grid = [[".","."],[".","."]]

Output: 0

Explanation:

No submatrix has at least one 'X'.

 

Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 'X', 'Y', or '.'.
'''
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        cols = [0]*n
        ans = 0
        other = [0]*n
        for i in range(m):
            row_sum = 0
            other_sum = 0
            for j in range(n):
                if grid[i][j] == 'X':
                    cols[j] += 1
                elif grid[i][j] == 'Y':
                    cols[j] -= 1
                else:
                    other[j] += 1
                row_sum += cols[j]
                other_sum += other[j]
                if row_sum == 0 and other_sum != (i+1)*(j+1):
                    ans += 1
        return ans
