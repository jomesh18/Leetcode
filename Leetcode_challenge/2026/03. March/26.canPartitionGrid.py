'''
3548. Equal Sum Grid Partition II
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of elements in both sections is equal, or can be made equal by discounting at most one single cell in total (from either section).
If a cell is discounted, the rest of the section must remain connected.
Return true if such a partition exists; otherwise, return false.

Note: A section is connected if every cell in it can be reached from any other cell by moving up, down, left, or right through other cells in the section.

 

Example 1:

Input: grid = [[1,4],[2,3]]

Output: true

Explanation:



A horizontal cut after the first row gives sums 1 + 4 = 5 and 2 + 3 = 5, which are equal. Thus, the answer is true.
Example 2:

Input: grid = [[1,2],[3,4]]

Output: true

Explanation:



A vertical cut after the first column gives sums 1 + 3 = 4 and 2 + 4 = 6.
By discounting 2 from the right section (6 - 2 = 4), both sections have equal sums and remain connected. Thus, the answer is true.
Example 3:

Input: grid = [[1,2,4],[2,3,5]]

Output: false

Explanation:



A horizontal cut after the first row gives 1 + 2 + 4 = 7 and 2 + 3 + 5 = 10.
By discounting 3 from the bottom section (10 - 3 = 7), both sections have equal sums, but they do not remain connected as it splits the bottom section into two parts ([2] and [5]). Thus, the answer is false.
Example 4:

Input: grid = [[4,1,8],[3,2,6]]

Output: false

Explanation:

No valid cut exists, so the answer is false.

 

Constraints:

1 <= m == grid.length <= 105
1 <= n == grid[i].length <= 105
2 <= m * n <= 105
1 <= grid[i][j] <= 105
'''
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        row_sum = [0]*m
        col_sum = [0]*n
        tot_sum = 0
        max_val = float('-inf')
        for i in range(m):
            for j in range(n):
                tot_sum += grid[i][j]
                row_sum[i] += grid[i][j]
                col_sum[j] += grid[i][j]
                max_val = max(max_val, grid[i][j])

        min_row = [-1]*(max_val+1)
        max_row = [-1]*(max_val+1)
        min_col = [-1]*(max_val+1)
        max_col = [-1]*(max_val+1)
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if min_row[val] == -1:
                    min_row[val] = i
                    max_row[val] = i
                    max_col[val] = j
                    min_col[val] = j
                else:
                    max_row[val] = i
                    max_col[val] = max(max_col[val], j)
                    min_col[val] = min(min_col[val], j)

        top = 0
        for i in range(m-1):
            print(i, 'top')
            top += row_sum[i]
            bottom = tot_sum - top
            if top == bottom:
                return True
            diff = abs(top-bottom)
            if diff > max_val or min_row[diff] == -1: continue
            if top > bottom:
                if min_row[diff] <= i:
                    if n == 1:
                        if grid[0][0] == diff or grid[i][0] == diff:
                            return True
                    elif i != 0:
                        return True
                    elif grid[0][0] == diff or grid[0][n-1] == diff:
                        return True
            else:
                if max_row[diff] > i:
                    if n == 1:
                        if grid[i+1][0] == diff or grid[m-1][0] == diff:
                            return True
                    elif i == m-2:
                        if grid[m-1][0] == diff or grid[m-1][n-1] == diff:
                            return True
                    else:
                        return True
        
        left = 0
        for j in range(n):
            left += col_sum[j]
            right = tot_sum - left
            if left == right:
                return True
            diff = abs(right-left)
            if diff > max_val or min_row[diff] == -1: continue
            if left > right:
                if min_col[diff] <= j:
                    if m == 1:
                        if grid[0][0] == diff or grid[0][j] == diff:
                            return True
                    elif j == 0:
                        if grid[0][0] == diff or grid[m-1][0] == diff:
                            return True
                    else:
                        return True
            else:
                if max_col[diff] > j:
                    if m == 1:
                        if grid[0][j+1] == diff or grid[0][n-1] == diff:
                            return True
                    elif j == m-2:
                        if grid[0][n-1] == diff or grid[m-1][n-1] == diff:
                            return True
                    else:
                        return True

        return False
