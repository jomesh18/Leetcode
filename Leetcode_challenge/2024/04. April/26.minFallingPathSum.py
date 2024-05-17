'''
1289. Minimum Falling Path Sum II
Hard

2219

122

Add to List

Share
Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

 

Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.
Example 2:

Input: grid = [[7]]
Output: 7
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
-99 <= grid[i][j] <= 99
'''
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1: return grid[0][0]
        def find_min_2_pos(i):
            min1, min2, pos1, pos2 = float('inf'), float('inf'), 0, 0
            for j, v in enumerate(grid[i]):
                if v <= min1:
                    min2 = min1
                    pos2 = pos1
                    pos1 = j
                    min1 = v
                elif v <= min2:
                    min2 = v
                    pos2 = j
            return min1, pos1, min2, pos2
            
        ans1, ans2, last1, last2 = 0, 0, -1, -1
        
        for i in range(1, n):
            min1, pos1, min2, pos2 = find_min_2_pos(i-1)
            for j in range(n):
                grid[i][j] += min1 if j != pos1 else min2
        return min(grid[-1])
