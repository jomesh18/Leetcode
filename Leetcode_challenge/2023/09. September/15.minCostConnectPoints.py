'''
1584. Min Cost to Connect All Points
Medium

4205

98

Add to List

Share
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        class UF:
            def __init__(self, n):
                self.root = [i for i in range(n)]
                self.rank = [1]*n
            
            def find(self, x):
                if self.root[x] != x:
                    self.root[x] = self.find(self.root[x])
                return self.root[x]
            
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return False
                if self.rank[px] > self.rank[py]:
                    self.root[py] = self.root[px]
                else:
                    self.root[px] = self.root[py]
                    if self.rank[px] == self.rank[py]:
                        self.rank[py] += 1
                return True
            
        dist_list = []
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1,len(points)):
                x2, y2 = points[j]
                dist_list.append((abs(x2-x1)+abs(y2-y1), i, j))

        dist_list.sort()
        uf = UF(len(points))
        ans = 0
        for dist, i, j in dist_list:
            if uf.union(i, j):
                ans += dist
        return ans