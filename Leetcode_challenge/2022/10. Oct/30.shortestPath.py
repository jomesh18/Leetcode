'''
1293. Shortest Path in a Grid with Obstacles Elimination
Hard

3734

67

Add to List

Share
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:


Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:


Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
'''
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        q = [(0, 0, k)]
        visited = {(0, 0, k)}
        level = 0
        while q:
            # print(q, level)
            newq = []
            for i, j, rem in q:
                if i == m-1 and j == n-1: return level
                for u, v in neighbors:
                    ni, nj = u+i, v+j
                    if 0<=ni<m and 0<=nj<n:
                        if grid[ni][nj] == 1 and rem > 0 and (ni, nj, rem-1) not in visited:
                                visited.add((ni, nj, rem-1))
                                newq.append((ni, nj, rem-1))
                        elif grid[ni][nj] == 0 and (ni, nj, rem) not in visited:
                                newq.append((ni, nj, rem))
                                visited.add((ni, nj, rem))
            q = newq[:]
            level += 1
        return -1