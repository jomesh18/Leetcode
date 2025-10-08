'''
417. Pacific Atlantic Water Flow
Solved
Medium
Topics
premium lock icon
Companies
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        connected_to_pacific = [[False]*n for _ in range(m)]
        visited = [[False]*n for _ in range(m)]
        pacific = deque([])

        for i in range(n):
            visited[0][i] = True
            connected_to_pacific[0][i] = True
            pacific.append((0, i))
        for i in range(1, m):
            visited[i][0] = True
            connected_to_pacific[i][0] = True
            pacific.append((i, 0))
        
        while pacific:
            i, j = pacific.popleft()
            for ni, nj in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if 0<=ni<m and 0<=nj<n and heights[i][j] <= heights[ni][nj] and not visited[ni][nj]:
                    visited[ni][nj] = True
                    connected_to_pacific[ni][nj] = True
                    pacific.append((ni, nj))

        atlantic = deque([])
        visited = [[False]*n for _ in range(m)]
        connected_to_atlantic = [[False]*n for _ in range(m)]

        for i in range(m):
            visited[i][n-1] = True
            connected_to_atlantic[i][n-1] = True
            atlantic.append((i, n-1))

        for i in range(n-1):
            visited[m-1][i] = True
            connected_to_atlantic[m-1][i] = True
            atlantic.append((m-1, i))

        while atlantic:
            i, j = atlantic.popleft()
            for ni, nj in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if 0<=ni<m and 0<=nj<n and heights[i][j] <= heights[ni][nj] and not visited[ni][nj]:
                    visited[ni][nj] = True
                    connected_to_atlantic[ni][nj] = True
                    atlantic.append((ni, nj))

        ans = []
        for i in range(m):
            for j in range(n):
                if connected_to_pacific[i][j] and connected_to_atlantic[i][j]:
                    ans.append([i, j])

        return ans
