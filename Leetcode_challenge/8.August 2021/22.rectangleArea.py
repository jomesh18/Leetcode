'''
Rectangle Area II
We are given a list of (axis-aligned) rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] , where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:


Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 1018 modulo (109 + 7), which is (109)2 = (-7)2 = 49.
 

Constraints:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 109
The total area covered by all rectangles will never exceed 263 - 1 and thus will fit in a 64-bit signed integer.
'''
class Solution:
    def rectangleArea(self, rectangles: [[int]]) -> int:
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        x_i = {v: i for i, v in enumerate(xs)}
        count = [0] * len(x_i)
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append([y1, x1, x2, 1])
            L.append([y2, x1, x2, -1])
        L.sort()
        cur_y = cur_x_sum = area = 0
        for y, x1, x2, sig in L:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            for i in range(x_i[x1], x_i[x2]):
                count[i] += sig
            cur_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))
        return area % (10 ** 9 + 7)

rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# Output: 6

rectangles = [[0,0,1000000000,1000000000]]
# # Output: 49

sol = Solution()
print(sol.rectangleArea(rectangles))
