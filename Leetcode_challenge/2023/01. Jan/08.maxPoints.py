'''
149. Max Points on a Line
Hard

3337

397

Add to List

Share
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
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(x, y):
            return gcd(y, x%y) if y else x
        ans = 1
        for i in range(len(points)):
            d = {}
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                x = x2-x1
                y = y2-y1
                g = gcd(x, y)
                x //= g
                y //= g
                key = str(x)+'_'+str(y)
                d[key] = d.get(key, 0) + 1
                ans = max(ans, d[key]+1)
        return ans