'''
934. Shortest Bridge
Medium

4659

178

Add to List

Share
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
'''
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        group1, group2 = set(), set()
        def dfs(i, j, visited):
            visited.add((i, j))
            for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ni, nj = i+di, j+dj
                if 0<=ni<m and 0<=nj<n and grid[ni][nj] == 1 and (ni, nj) not in visited:
                    dfs(ni, nj, visited)
                
        for i in range(m):
            if group2: break
            for j in range(n):
                if grid[i][j] == 1:
                    if not group1:
                        dfs(i, j, group1)
                    elif (i, j) in group1:
                        continue
                    else:
                        dfs(i, j, group2)
                        break
        
        q = list(group1)
        level = 0
        while q:
            nq = []
            for i, j in q:
                for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    ni, nj = i+di, j+dj
                    if 0<=ni<m and 0<=nj<n and (ni, nj) not in group1:
                        if grid[ni][nj] == 1:
                            return level
                        else:
                            group1.add((ni, nj))
                            nq.append((ni, nj))
            q = nq
            level += 1
        
        return -1