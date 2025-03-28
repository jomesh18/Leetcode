'''
2503. Maximum Number of Points From Grid Queries
Solved
Hard
Topics
Companies
Hint
You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.

 

Example 1:


Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.
Example 2:


Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
k == queries.length
1 <= k <= 104
1 <= grid[i][j], queries[i] <= 106
'''
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
        def dfs(i, j, num, visited, ends):
            if grid[i][j] >= num:
                ends.add((i, j))
                return

            self.ans += 1
            visited[i][j] = True
            for ni, nj in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if 0<=ni<m and 0<=nj<n and not visited[ni][nj]:
                    dfs(ni, nj, num, visited, ends)
        
        query_dict = {}
        for i, q in enumerate(queries):
            if q not in query_dict:
                query_dict[q] = []
            query_dict[q].append(i)

        m, n = len(grid), len(grid[0])
        answer = [0]*len(queries)
        ends = {(0, 0)}
        visited = [[False]*n for _ in range(m)]
        self.ans = 0

        for q in sorted(query_dict.keys()):
            new_ends = set()
            for a, b in ends:
                if not visited[a][b]:
                    dfs(a, b, q, visited, new_ends)

            for i in query_dict[q]:
                answer[i] = self.ans
            ends = new_ends
        return answer
