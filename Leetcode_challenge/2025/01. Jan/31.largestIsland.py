'''
827. Making A Large Island
Solved
Hard
Topics
Companies
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
'''
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        class UF:
            def __init__(self, n):
                self.root = [i for i in range(n)]
                self.rank = [1]*n
                self.count = [1]*n
            
            def find(self, x):
                if self.root[x] != x:
                    self.root[x] = self.find(self.root[x])
                return self.root[x]

            def union(self, x, y):
                rx, ry = self.find(x), self.find(y)
                if rx != ry:
                    if self.rank[rx] >= self.rank[ry]:
                        self.root[ry] = rx
                        self.count[rx] += self.count[ry]
                        if self.rank[rx] == self.rank[ry]:
                            self.rank[rx] += 1
                    else:
                        self.root[rx] = ry
                        self.count[ry] += self.count[rx]
        uf = UF(n*n)

        def dfs(i, j, uf, visited):
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0<=ni<n and 0<=nj<n and not visited[ni][nj] and grid[ni][nj] == 1:
                    visited[ni][nj] = True
                    uf.union(i*n+j, ni*n+nj)
                    dfs(ni, nj, uf, visited)

        visited = [[False]*n for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    visited[i][j] = True
                    dfs(i, j, uf, visited)
                    ans = max(ans, uf.count[i*n+j])
        # print(uf.root)
        # print(uf.count)
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                groups = set()
                pos = []
                if i-1 >= 0 and grid[i-1][j] == 1:
                    pos.append((i-1)*n+j)
                if i+1 < n and grid[i+1][j] == 1:
                    pos.append((i+1)*n+j)
                if j-1 >= 0 and grid[i][j-1] == 1:
                    pos.append(i*n+j-1)
                if j+1 < n and grid[i][j+1] == 1:
                    pos.append(i*n+j+1)
                for p in pos:
                    groups.add(uf.find(p))
                # print(groups)
                temp = 1
                for g in groups:
                    temp += uf.count[g]
                ans = max(ans, temp)
            
        return ans