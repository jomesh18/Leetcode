'''
223. Rectangle Area
Medium

1145

1268

Add to List

Share
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

 

Example 1:

Rectangle Area
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45
Example 2:

Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16
 

Constraints:

-104 <= ax1 <= ax2 <= 104
-104 <= ay1 <= ay2 <= 104
-104 <= bx1 <= bx2 <= 104
-104 <= by1 <= by2 <= 104
'''
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a3 = 0
        if ((ax1 <= bx1 < ax2) or (bx1 <= ax1 < bx2)) and ((ay1 <= by1 < ay2) or (by1 <= ay1 < by2)):
            cx1 = max(ax1, bx1)
            cx2 = min(ax2, bx2)
            cy1 = max(ay1, by1)
            cy2 = min(ay2, by2)
            a3 = (cx2-cx1) * (cy2-cy1)
        a1 = (ax2-ax1) * (ay2-ay1)
        a2 = (bx2-bx1) * (by2-by1)
        return a1 + a2 - a3