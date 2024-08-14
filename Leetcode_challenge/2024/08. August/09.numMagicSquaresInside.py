'''
840. Magic Squares In Grid
Medium

555

1702

Add to List

Share
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

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
        count = 0
        def ok(i, j):
            nums = set()
            for r in range(i, i+3):
                for c in range(j, j+3):
                    nums.add(grid[r][c])
            if len(nums) != 9: return False
            for k in range(1, 10):
                if k not in nums: return False
            s = 0
            for c in range(j, j+3, 1):
                s += grid[i][c]
            for r in range(i, i+3):
                curr_s = 0
                for c in range(j, j+3):
                    curr_s += grid[r][c]
                if curr_s != s: return False
            for c in range(j, j+3):
                curr_s = 0
                for r in range(i, i+3):
                    curr_s += grid[r][c]
                if curr_s != s: return False
            diag1 = 0
            diag2 = 0
            for k in range(3):
                diag1 += grid[i+k][j+k]
                diag2 += grid[i+k][j+2-k]
            # print(diag1, diag2)
            if diag2 != s or diag1 != s:
                return False
            return True

        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if ok(i, j):
                    count += 1
        return count