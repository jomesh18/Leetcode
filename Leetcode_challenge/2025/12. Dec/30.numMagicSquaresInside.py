'''
840. Magic Squares In Grid
Solved
Medium
Topics
premium lock icon
Companies
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

 

Example 1:


Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.
Example 2:

Input: grid = [[8]]
Output: 0
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
'''
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def ok(i, j):
            found = set()
            mat = [grid[i][j:j+3], grid[i+1][j:j+3], grid[i+2][j:j+3]]
            s = sum(mat[0])
            d_sum = 0
            ad_sum = 0
            c1, c2, c3 = 0, 0, 0
            for r in range(3):
                for c in range(3):
                    if r == c:
                        d_sum += mat[r][c]
                    if r + c == 2:
                        ad_sum += mat[r][c]
                    if c == 0:
                        c1 += mat[r][c]
                    elif c == 1:
                        c2 += mat[r][c]
                    elif c == 2:
                        c3 += mat[r][c]
                    if mat[r][c] > 9 or mat[r][c] < 1: return False
                    found.add(mat[r][c])
            # print(found, d_sum, ad_sum, s)
            # print(c1, c2, c3)
            # print(sum(mat[1]), sum(mat[2]))
            if len(found) != 9: return False
            if s != d_sum or s != ad_sum: return False
            if s != sum(mat[1]) or s != sum(mat[2]): return False
            if c1 != c2 != c3 != s: return False
            return True

        ans = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if ok(i, j): ans += 1
        return ans
