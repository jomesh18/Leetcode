'''
3625. Count Number of Trapezoids II
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D integer array points where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

Return the number of unique trapezoids that can be formed by choosing any four distinct points from points.

A trapezoid is a convex quadrilateral with at least one pair of parallel sides. Two lines are parallel if and only if they have the same slope.

 

Example 1:

Input: points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]

Output: 2

Explanation:



There are two distinct ways to pick four points that form a trapezoid:

The points [-3,2], [2,3], [3,2], [2,-3] form one trapezoid.
The points [2,3], [3,2], [3,0], [2,-3] form another trapezoid.
Example 2:

Input: points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:



There is only one trapezoid which can be formed.

 

Constraints:

4 <= points.length <= 500
–1000 <= xi, yi <= 1000
All points are pairwise distinct.
'''
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        d = {}
        mids = {}
        inf = 10**9 + 7
        for i in range(n-1):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                if dx == 0:
                    m = inf
                    c = x1
                else:
                    m = dy/dx
                    c = (y1*dx - x1*dy)/dx
                if m not in d:
                    d[m] = {}
                if c not in d[m]:
                    d[m][c] = 0
                d[m][c] += 1

                k = (x1 + x2) * 10000 + (y1 + y2)
                if k not in mids:
                    mids[k] = {}
                if m not in mids[k]:
                    mids[k][m] = 0
                mids[k][m] += 1

        ans = 0
        for m in d:
            s = 0
            if len(d[m]) > 1:
                for c in d[m]:
                    ans += s * d[m][c]
                    s += d[m][c]
        
        for k in mids:
            s = 0
            if len(mids[k]) > 1:
                for m in mids[k]:
                    ans -= s*mids[k][m]
                    s += mids[k][m]
        return ans
