'''
417. Pacific Atlantic Water Flow
Medium

4849

976

Add to List

Share
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
        
        can_reach_pacific = set([(0, j) for j in range(n)]+[(i, 0) for i in range(1, m)])
        can_reach_atlantic = set([(i, n-1) for i in range(m)]+[(m-1, j) for j in range(n-1)])
            
        def dfs(i, j, visited, place):
            if (i, j) in place:
                return True
            for u, v in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if 0<=u<m and 0<=v<n and (u, v) not in visited and heights[u][v] <= heights[i][j]:
                    visited.add((u, v))
                    if dfs(u, v, visited, place): return True
                    visited.remove((u, v))
            return False
            
        for i in range(m):
            for j in range(n):
                if dfs(i, j, {(i, j)}, can_reach_pacific):
                    can_reach_pacific.add((i, j))
                if dfs(i, j, {(i, j)}, can_reach_atlantic):
                    can_reach_atlantic.add((i, j))
        
        return can_reach_pacific.intersection(can_reach_atlantic)


#from ocean flood fill
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        a_visited = [[False]*n for _ in range(m)]
        p_visited = [[False]*n for _ in range(m)]
        
        def dfs(i, j, visited):
            visited[i][j] = True
            for u, v in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if 0<=u<m and 0<=v<n and not visited[u][v] and heights[u][v] >= heights[i][j]:
                    dfs(u, v, visited)
        
        for i in range(m):
            dfs(i, 0, p_visited)
            dfs(i, n-1, a_visited)
            
        for i in range(n):
            dfs(0, i, p_visited)
            dfs(m-1, i, a_visited)
            
        ans = []
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    ans.append([i, j])
        return ans
        