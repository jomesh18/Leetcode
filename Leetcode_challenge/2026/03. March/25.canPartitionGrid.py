'''
3546. Equal Sum Grid Partition I
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of the elements in both sections is equal.
Return true if such a partition exists; otherwise return false.

 

Example 1:

Input: grid = [[1,4],[2,3]]

Output: true

Explanation:



A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.

Example 2:

Input: grid = [[1,3],[2,4]]

Output: false

Explanation:

No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.

 

Constraints:

1 <= m == grid.length <= 105
1 <= n == grid[i].length <= 105
2 <= m * n <= 105
1 <= grid[i][j] <= 105
'''
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        s = sum(sum(row) for row in grid)
        if s & 1: return False
        half = s//2
        s = 0
        for row in grid:
            s += sum(row)
            if s ==  half:
                return True
            if s > half:
                break
        s = 0
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                s += grid[i][j]
            if s == half:
                return True
            if s > half:
                break
        return False
