'''
1584. Min Cost to Connect All Points
Medium

1700

54

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
Accepted
68,153
Submissions
109,262
Seen this question in a real interview before?

Yes

No
'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        class Edge:
            def __init__(self, point1, point2, cost):
                self.point1 = point1
                self.point2 = point2
                self.cost = cost
                
            def __lt__(self, e):
                return self.cost < e.cost
            
        class UF:
            def __init__(self, size):
                self.root = [i for i in range(size)]
                self.rank = [0]*size
                
            def find(self, x):
                if x == self.root[x]:
                    return x
                self.root[x] = self.find(self.root[x])
                return self.root[x]
            
            def union(self, x, y):
                px = self.find(x)
                py = self.find(y)
                
                if px != py:
                    if self.rank[px] > self.rank[py]:
                        self.root[py] = px
                    elif self.rank[py] > self.rank[px]:
                        self.root[px] = py
                    else:
                        self.root[py] = px
                        self.rank[px] += 1
                
            def connected(self, x, y):
                return self.find(x) == self.find(y)
            
        n = len(points)
        uf = UF(n)
        pq = []
        for i in range(n):
            for j in range(i+1, n):
                cost = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                e = Edge(i, j, cost)
                heapq.heappush(pq, e)
        
        p = n-1
        ans = 0
        while pq and p:
            e = heapq.heappop(pq)
            if not uf.connected(e.point1, e.point2):
                ans += e.cost
                uf.union(e.point1, e.point2)
                p -= 1
        return ans
        