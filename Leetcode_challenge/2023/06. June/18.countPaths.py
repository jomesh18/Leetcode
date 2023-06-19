'''
2328. Number of Increasing Paths in a Grid
Hard

1691

39

Add to List

Share
You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.

Two paths are considered different if they do not have exactly the same sequence of visited cells.

 

Example 1:


Input: grid = [[1,1],[3,4]]
Output: 8
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [1], [3], [4].
- Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
- Paths with length 3: [1 -> 3 -> 4].
The total number of paths is 4 + 3 + 1 = 8.
Example 2:

Input: grid = [[1],[2]]
Output: 3
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [2].
- Paths with length 2: [1 -> 2].
The total number of paths is 2 + 1 = 3.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
1 <= grid[i][j] <= 105
'''
# O(m*n log(m*n))
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[1]*n for _ in range(m)]
        cell_list = [[i, j] for i in range(m) for j in range(n)]
        cell_list.sort(key=lambda x:grid[x[0]][x[1]])
        
        MOD = 10**9+7
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        
        for i, j in cell_list:
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<m and 0<=nj<n and grid[ni][nj] > grid[i][j]:
                    dp[ni][nj] += dp[i][j]
                    dp[ni][nj] %= MOD
        return sum(sum(row)%MOD for row in dp)%MOD


#O(m*n)
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9+7
        dp = [[0]*n for _ in range(m)]
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        
        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]
            ans = 1
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<m and 0<=nj<n and grid[ni][nj] < grid[i][j]:
                    ans += dfs(ni, nj)%mod
            dp[i][j] = ans
            return ans
        
        return sum(dfs(i, j) for i in range(m) for j in range(n))%mod