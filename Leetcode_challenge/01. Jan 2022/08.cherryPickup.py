'''
1463. Cherry Pickup II
Hard

1232

15

Add to List

Share
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

Robot #1 is located at the top-left corner (0, 0), and
Robot #2 is located at the top-right corner (0, cols - 1).
Return the maximum number of cherries collection using both robots by following the rules below:

From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
When both robots stay in the same cell, only one takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in grid.
 

Example 1:


Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.
Example 2:


Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.
 

Constraints:

rows == grid.length
cols == grid[i].length
2 <= rows, cols <= 70
0 <= grid[i][j] <= 100

'''
#top down, memoization
# class Solution:
#     def cherryPickup(self, grid: [[int]]) -> int:
#         row, cols = len(grid), len(grid[0])
#         #move the robots synchronously
#         #row, col1 is pos of robot1 and row, col2 is pos of robot 2
#         #dp[row, col1, col2] is the maximun no of cherries we can get if robot1 starts at row, col1 and 
#         #robot2 at row, col2
        
#         dp = {}
        
#         def helper(r, col1, col2):
#             if col1<0 or col1>= cols or col2<0 or col2 >= cols: return 0
#             if (r, col1, col2) in dp: return dp[(r, col1, col2)]
            
#             res = 0
#             res += grid[r][col1]
#             if col1 != col2: res += grid[r][col2]
            
#             if r != row-1:
#                 temp = 0
#                 for i in [col1, col1+1, col1-1]:
#                     for j in [col2, col2+1, col2-1]:
#                         temp = max(temp, helper(r+1, i, j))
#                 res += temp
#             dp[(r, col1, col2)] = res
#             return res

#         return helper(0, 0, cols-1)

#bottom up, dp
class Solution:
    def cherryPickup(self, grid: [[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[[0]*n for _ in range(n)] for _ in range(m)]

        for row in reversed(range(m)):
            for col1 in range(n):
                for col2 in range(n):
                    res = 0
                    res += grid[row][col1]
                    if col1 != col2:
                        res += grid[row][col2]
                    if row != m-1:
                        res += max(dp[row+1][c1][c2] for c1 in [col1, col1+1, col1-1] 
                                   for c2 in [col2, col2+1, col2-1] if 0<=c1<n and 0<=c2<n)
                    dp[row][col1][col2] = res
        return dp[0][0][n-1]


grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# Output: 24

# grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
# Output: 28

sol = Solution()
print(sol.cherryPickup(grid))
