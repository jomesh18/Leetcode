'''
1895. Largest Magic Square
Solved
Medium
Topics
premium lock icon
Companies
Hint
A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

 

Example 1:


Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
Output: 3
Explanation: The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12
Example 2:


Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
Output: 2
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 106
'''
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def find_sums(r, c, k):
            rows = [0]*k
            cols = [0]*k
            for i in range(r, r+k):
                for j in range(c, c+k):
                    rows[i-r] += grid[i][j]
                    cols[j-c] += grid[i][j]
            s = rows[0]
            for i in range(k):
                if rows[i] != s:
                    return False
                if cols[i] != s:
                    return False
            diag = 0
            anti_diag = 0
            for i in range(k):
                diag += grid[r+i][c+i]
                anti_diag += grid[r+i][c+k-1-i]
            if s != diag:
                return False
            if s != anti_diag:
                return False
            
            return True

        max_k = min(m, n)
        for k in range(max_k, 0, -1):
            for i in range(m-k+1):
                for j in range(n-k+1):
                    if find_sums(i, j, k):
                        return k
        