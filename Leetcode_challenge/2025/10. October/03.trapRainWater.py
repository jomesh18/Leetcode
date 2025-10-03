'''
407. Trapping Rain Water II
Solved
Hard
Topics
premium lock icon
Companies
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
 

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
'''
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        boundaries = []
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            heappush(boundaries, (heightMap[i][0], i, 0))
            heappush(boundaries, (heightMap[i][n-1], i, n-1))
            visited[i][0] = True
            visited[i][n-1] = True

        for i in range(n):
            heappush(boundaries, (heightMap[0][i], 0, i))
            heappush(boundaries, (heightMap[m-1][i], m-1, i))
            visited[0][i] = True
            visited[m-1][i] = True

        water = 0
        while boundaries:
            h, r, c = heappop(boundaries)
            for nr, nc in [(r-1, c), (r, c-1), (r, c+1), (r+1, c)]:
                if 0<=nr<m and 0<=nc<n and not visited[nr][nc]:
                    if heightMap[nr][nc] < h:
                        water += h-heightMap[nr][nc]
                    visited[nr][nc] = True
                    heappush(boundaries, (max(h, heightMap[nr][nc]), nr, nc))
        
        return water
