'''
3197. Find the Minimum Area to Cover All Ones II
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.

Return the minimum possible sum of the area of these rectangles.

Note that the rectangles are allowed to touch.

 

Example 1:

Input: grid = [[1,0,1],[1,1,1]]

Output: 5

Explanation:



The 1's at (0, 0) and (1, 0) are covered by a rectangle of area 2.
The 1's at (0, 2) and (1, 2) are covered by a rectangle of area 2.
The 1 at (1, 1) is covered by a rectangle of area 1.
Example 2:

Input: grid = [[1,0,1,0],[0,1,0,1]]

Output: 5

Explanation:



The 1's at (0, 0) and (0, 2) are covered by a rectangle of area 3.
The 1 at (1, 1) is covered by a rectangle of area 1.
The 1 at (1, 3) is covered by a rectangle of area 1.
 

Constraints:

1 <= grid.length, grid[i].length <= 30
grid[i][j] is either 0 or 1.
The input is generated such that there are at least three 1's in grid.
'''
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def min_area(sr, er, sc, ec):
            end_row, start_row, end_col, start_col = -1, m, -1, n
            found = False
            for i in range(sr, er+1):
                for j in range(sc, ec+1):
                    if grid[i][j]:
                        start_row = min(start_row, i)
                        end_row = max(end_row, i)
                        start_col = min(start_col, j)
                        end_col = max(end_col, j)
                        found = True
            return 0 if not found else (end_row-start_row+1) * (end_col-start_col+1)


        # Case 1
        # -------------
        # |    (1)    |
        # |           |
        # -------------
        # | (2) | (3) |
        # |     |     |
        # -------------
        # 
        ans = m * n
        for i in range(m):
            one = min_area(0, i, 0, n-1)
            for j in range(n):
                two = min_area(i+1, m-1, 0, j)
                three = min_area(i+1, m-1, j+1, n-1)
                ans = min(ans, one+two+three)
    
        # Case 2
        # -------------
        # |     | (2) |
        # |     |     |
        #   (1) -------
        # |     |     |
        # |     | (3) |
        # -------------
        
        for j in range(n):
            one = min_area(0, m-1, 0, j)
            for i in range(m):
                two = min_area(0, i, j+1, n-1)
                three = min_area(i+1, m-1, j+1, n-1)
                ans = min(ans, one+two+three)
    
        # Case 3
        # -------------
        # |     |     |
        # | (2) |     |
        # ------- (1) |
        # |     |     |
        # | (3) |     |
        # -------------
        for j in range(n-1, -1, -1):
            one = min_area(0, m-1, j+1, n-1)
            for i in range(m):
                two = min_area(0, i, 0, j)
                three = min_area(i+1, m-1, 0, j)
                ans = min(ans, one+two+three)
    
        # Case 4
        # -------------
        # | (2) | (3) |
        # |     |     |
        # ------------
        # |           |
        # |    (1)    |
        # -------------

        for i in range(m-1, -1, -1):
            one = min_area(i+1, m-1, 0, n-1)
            for j in range(n):
                two = min_area(0, i, 0, j)
                three = min_area(0, i, j+1, n-1)
                ans = min(ans, one+two+three)

        # Case 5
        # -------------
        # |    (1)    |
        # -------------
        # |    (2)    |
        # -------------
        # |    (3)    |
        # -------------

        for i in range(m):
            one = min_area(0, i, 0, n-1)
            for j in range(i+1, m):
                two = min_area(i+1, j, 0, n-1)
                three = min_area(j+1, m-1, 0, n-1)
                ans = min(ans, one+two+three)

        #  Case 6
        # -------------
        # |   |   |   |
        # |   |   |   |
        # |(1)|(2)|(3)|
        # |   |   |   |
        # |   |   |   |
        # -------------
        
        for i in range(n):
            one = min_area(0, m-1, 0, i)
            for j in range(i+1, n):
                two = min_area(0, m-1, i+1, j)
                three = min_area(0, m-1, j+1, n-1)
                ans = min(ans, one+two+three)

        return ans
