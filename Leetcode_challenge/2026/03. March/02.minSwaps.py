'''
1536. Minimum Swaps to Arrange a Binary Grid
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

 

Example 1:


Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
Example 2:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.
Example 3:


Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
grid[i][j] is either 0 or 1
'''
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_right_one = [0]*n
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    max_right_one[i] = j
        
        sorted_max_right = sorted(max_right_one)
        for i in range(n):
            if i < sorted_max_right[i]: return -1

        ans = 0
        for i in range(n):
            for j in range(i, n):
                if max_right_one[j] <= i:
                    ans += j-i
                    popped = max_right_one.pop(j)
                    max_right_one.insert(i, popped)
                    break
        
        return ans  
