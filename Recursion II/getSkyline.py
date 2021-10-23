'''
The Skyline Problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

    lefti is the x coordinate of the left edge of the ith building.
    righti is the x coordinate of the right edge of the ith building.
    heighti is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

 

Example 1:

Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.

Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]

 

Constraints:

    1 <= buildings.length <= 104
    0 <= lefti < righti <= 231 - 1
    1 <= heighti <= 231 - 1
    buildings is sorted by lefti in non-decreasing order.

'''
#memory exceeded
# class Solution:
#     def getSkyline(self, buildings: [[int]]) -> [[int]]:
#         lower, upper = buildings[0][0], buildings[-1][1]
#         res = [0] * (upper-lower)
#         for b in buildings:
#             left, right, height = b
#             for i in range(left-lower, right-lower):
#                 res[i] = height if height > res[i] else res[i]
#         ans = [[lower, res[0]]]
#         for i in range(1, len(res)):
#             if res[i] != res[i-1]:
#                 ans.append([i+lower, res[i]])
#         ans.append([upper, 0])
#         return ans

#using heapq, youtube tushar's explanation
# import heapq
# class Solution:
#     def getSkyline(self, buildings: [[int]]) -> [[int]]:
#         res = []
#         building_points = []
#         for b in buildings:
#             building_points.extend([(b[0], b[2], 1), (b[1], b[2], 0)])
#         building_points.sort(key=lambda x: (x[0], -x[1] if x[2] else x[0], x[1]))
#         # print(building_points)
#         l = [0]
#         for b in building_points:
#             old_max = -l[0]
#             x, y, is_start = b
#             if is_start:
#                 heapq.heappush(l, -y)
#             else:
#                 l.remove(-y)
#                 heapq.heapify(l)
#             if -l[0] != old_max:
#                 res.append((x, -l[0]))
#         return res

import heapq
class Solution:
    def getSkyline(self, buildings):
        def draw_to_sky(t, h):
            if sky[-1][1] != h:
                sky.append([t, h])

        positions = set([b[0] for b in buildings]+[b[1] for b in buildings])
        sky = [[-1, 0]]
        live = []
        i = 0
        for t in sorted(positions):
            while i < len(buildings) and buildings[i][0] <= t:
                heapq.heappush(live, (-buildings[i][2], buildings[i][1]))
                i += 1
            while live and live[0][1] <= t:
                heapq.heappop(live)
            h = -live[0][0] if live else 0
            draw_to_sky(t, h)
        return sky[1:]

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

buildings = [[0,2,3],[2,5,3]]
# # Output: [[0,3],[5,0]]

buildings = [[0,2147483647,2147483647]]
# # Output: 

# buildings = [[0, 1, 2], [0, 2, 3], [3, 5, 3], [4, 5, 2], [6, 7, 2], [7, 8, 3]]
# Output: [[0, 3], [2, 0], [3, 3], [5, 0], [6, 2], [7, 3], [8, 0]]

sol = Solution()
print(sol.getSkyline(buildings))
