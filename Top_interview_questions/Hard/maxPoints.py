'''
Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
'''
# using equation of a line with two points: (x-x1)/(x2-x1) = (y-y1)/(y2-y1)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 1
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                count = 0
                x2, y2 = points[j]
                a = x2-x1
                b = y2-y1
                for k in range(n):
                    x3, y3 = points[k]
                    if b*(x3-x1) == (y3-y1)*a:
                        count += 1
                ans = max(ans, count)
        return ans