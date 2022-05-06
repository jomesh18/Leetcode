'''
1631. Path With Minimum Effort
Medium

2585

113

Add to List

Share
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
 

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
Accepted
87,700
Submissions
164,123
'''
#dfs and binary search
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        
        def valid(mid, i=0, j=0, visited={(0, 0)}):
            if i == m-1 and j == n-1:
                return True
            ans = False
            for u, v in ((i, j+1), (i+1, j), (i-1, j), (i, j-1)):
                if 0<=u<m and 0<=v<n and (u, v) not in visited:
                    curr_diff = abs(heights[i][j]-heights[u][v])
                    if curr_diff > mid: continue
                    visited.add((u, v))
                    ans |= valid(mid, u, v, visited)
                    if ans: return ans
            return ans                                      
             
        lo, hi = 0, max(max(l) for l in heights)
        while lo < hi:
            mid = lo + ((hi-lo)>>1)
            if valid(mid, 0, 0, {(0, 0)}):
                hi = mid
            else:
                lo = mid+1
        return lo

#dfs and binary search
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        
        def dfs(mid, i, j, visited):
            if i == m-1 and j == n-1: return True
            visited[i][j] = True
            for u, v in ((i, j+1), (i+1, j), (i-1, j), (i, j-1)):
                if 0<=u<m and 0<=v<n and not visited[u][v]:
                    if abs(heights[i][j]-heights[u][v]) > mid: continue
                    if dfs(mid, u, v, visited): return True
            return False
        
        def valid(mid):
            return dfs(mid, 0, 0, [[False]*n for _ in range(m)])
             
        lo, hi = 0, max(max(l) for l in heights)
        while lo < hi:
            mid = lo + ((hi-lo)>>1)
            if valid(mid):
                hi = mid
            else:
                lo = mid+1
        return lo

#dijikstra
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        minheap = [(0, 0, 0)] #distance, r, c
        distance = [[10**6]*n for _ in range(m)]
        distance[0][0] = 0
        neighbours = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while minheap:
            d, r, c = heapq.heappop(minheap)
            if r == m-1 and c ==  n-1: return d
            if d > distance[r][c]: continue
            for dx, dy in neighbours:
                nr, nc = r+dx, c+dy
                if 0<= nr < m and 0<=nc<n:
                    nd = max(d, abs(heights[nr][nc]-heights[r][c]))
                    if distance[nr][nc] > nd:
                        distance[nr][nc] = nd
                        heapq.heappush(minheap, (nd, nr, nc))
