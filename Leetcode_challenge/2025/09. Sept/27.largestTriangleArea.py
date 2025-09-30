'''
812. Largest Triangle Area
Solved
Easy
Topics
premium lock icon
Companies
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:


Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
 

Constraints:

3 <= points.length <= 50
-50 <= xi, yi <= 50
All the given points are unique.
 

'''
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        def find_side(i, j):
            x1, y1 = points[i]
            x2, y2 = points[j]
            return ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)) ** .5

        ans = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    a = find_side(i, j)
                    b = find_side(i, k)
                    c = find_side(j, k)
                    if max(a, b, c) >= (a+b+c) - max(a, b, c):
                        continue
                    s = (a + b + c) / 2
                    curr = (s*(s-a)*(s-b)*(s-c))**.5
                    ans = max(ans, curr)
        
        return ans
